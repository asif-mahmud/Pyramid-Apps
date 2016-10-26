from . import globalvars
import os
import shutil
from uuid import uuid4
from sqlalchemy import (
    Column,
    Text,
    ARRAY,
)
from sqlalchemy.orm import Query
from .func import get_validator_status
from .func import get_image_writer
import logging


log = logging.getLogger(__name__)


class BaseImage(object):
    """Base image class to be used as Image entity's parent.

    Attributes:
        basename(str):
            The base file name in ``temporary`` folder or the base folder name
            in the ``persistent`` folder.

        image_type(str):
            Image codec name for ``imageio``.

        extension(str):
            Image file extension in the ``persistent`` folder.

    Properties:
        available_sizes(list(tuple(int, int))):
            Available/Pending to be written image sizes/thumbnails in the
            persistent folder.
    """

    basename = Column(Text, nullable=False, unique=True)
    _available_sizes = Column(ARRAY(Text), nullable=False)
    image_type = Column(Text, nullable=False)
    extension = Column(Text, nullable=False)

    def from_file_obj(self,
                      file_obj,
                      validate=True):
        """Tries to download the file to ``temporary`` folder.

        Returns:
            ``None`` if does not succeed else the full file path of the
            ``temporary`` file.
        """
        if globalvars.image_storage is None:
            raise OSError('No Image storage')

        # Find a suitable non-existent file name
        filename = None
        basename = None
        for cnt in range(0, 10):
            basename = uuid4().hex
            filename = os.path.join(
                globalvars.image_storage.persistent,
                basename,
            )
            if not os.path.exists(filename):
                filename = os.path.join(
                    globalvars.image_storage.temporary,
                    basename,
                )
                break
        else:
            raise OSError("No Suitable file name")

        # Try to downlaod the file object.
        try:
            with open(filename, 'wb') as output_file:
                shutil.copyfileobj(file_obj, output_file)
        except Exception as err:
            raise err

        if validate:
            vstatus = self.validate(temp_filename=filename)
            if vstatus is not None:
                self.basename = basename
            else:
                return None

        return filename

    def validate(self, temp_filename=None):
        vstatus = get_validator_status(temp_filename)
        if vstatus is not None:
            if self._available_sizes is None:
                self._available_sizes = list()
            self._available_sizes.append(
                '{}x{}'.format(
                    vstatus.size[0],
                    vstatus.size[1]
                )
            )
            self.image_type = vstatus.type
            self.extension = vstatus.extension
            return vstatus

    @property
    def available_sizes(self):
        return [
            (
                int(size.split('x')[0]),
                int(size.split('x')[1])
            ) for size in self._available_sizes
        ]

    @property
    def max_size(self):
        m_size = (0, 0)
        for size in self.available_sizes:
            if (m_size[0] * m_size[1]) < (size[0] * size[1]):
                m_size = size
        return m_size

    def get_url(self, size=None):
        if not size:
            size = self.available_sizes[0]
        image_filename = '{}x{}.{}'.format(
            size[0],
            size[1],
            self.extension
        )
        # /persistent_path/basename/image_size.ext
        return os.path.join(
            globalvars.image_storage.persistent,
            self.basename,
            image_filename,
        )

    def add_thumbnail(self, size=None):
        if size:
            self._available_sizes.append(
                '{}x{}'.format(
                    size[0],
                    size[1],
                )
            )


class BaseImageQuery(Query):
    """Query class to track all ``image`` instances."""

    _images_to_write = list()
    _images_to_delete = list()

    @classmethod
    def after_insert(cls, mapper, connection, target):
        cls._images_to_write.append(target)

    @classmethod
    def after_delete(cls, mapper, connection, target):
        cls._images_to_delete.append(target)

    @classmethod
    def after_soft_rollback(cls, session, previous_transaction):
        for img in cls._images_to_write:
            writer = get_image_writer(img)
            writer.clean_up()
        for img in cls._images_to_delete:
            writer = get_image_writer(img)
            writer.clean_up()
        cls._images_to_write.clear()
        cls._images_to_delete.clear()

    @classmethod
    def after_commit(cls, session):
        for img in cls._images_to_write:
            writer = get_image_writer(img)
            writer.write_all()
        for img in cls._images_to_delete:
            writer = get_image_writer(img)
            writer.delete_all()
        cls._images_to_write.clear()
        cls._images_to_delete.clear()
