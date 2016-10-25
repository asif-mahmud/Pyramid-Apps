from imageupload.models.storage.image.validators import (
    get_validator_status,
)
from imageupload.models.storage.image import image_storage
import os
import shutil
from uuid import uuid4
from sqlalchemy import (
    Column,
    Text,
    ARRAY,
)


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

        available_sizes(list(tupple(int, int))):
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
            ``None`` if does not succeed else the base file name in the
            ``temporary`` folder.
        """
        if image_storage is None:
            return None

        # Find a suitable non-existent file name
        filename = None
        basename = None
        for cnt in range(0, 10):
            basename = uuid4().hex
            filename = os.path.join(
                image_storage.persistent,
                basename,
            )
            if not os.path.exists(filename):
                filename = os.path.join(
                    image_storage.temporary,
                    basename,
                )
                break
        else:
            return None

        # Try to downlaod the file object.
        try:
            with open(filename, 'wb') as output_file:
                shutil.copyfileobj(file_obj, output_file)
        except Exception:
            return None

        if validate:
            vstatus = self.validate(temp_filename=filename)
            if vstatus is not None:
                self.basename = basename

        return filename

    def validate(self, temp_filename=None):
        vstatus = get_validator_status(temp_filename)
        if vstatus is not None:
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
            image_storage.persistent,
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
