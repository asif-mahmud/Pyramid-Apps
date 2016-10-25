import os
from pathlib import Path


class StorageSingleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(StorageSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class BaseStorageInfo(object, metaclass=StorageSingleton):
    """Base class for any storage info provider.

    Every storage info provider will provide 2 absolute directory
    paths. One for ``temporary`` and other for ``persistent``.
    ``temporary`` is the directory where all the immediate uploads
    take place and the ``persistent`` is the place where the database
    ready files are written.

    Particular storage should provide one and only one instance of their
    own ``StorageInfo`` at the startup of the app.

    Child ``StorageInfo`` classes must define at least 1 property -

        1. _prefix(must define): A storage prefix for the specific storage.
        2. _temporary(optional): Temporary sub-folder's name.
        3. _persistent(optional): Persistent sub-folder's name.

    Usage:
        ```
        class ImageStorageInfo(BaseStorageInfo):
            _prefix = 'images'

        ```

        Create one instance in the infamous ``includeme`` function. Make it
        global.
    """

    _prefix = None
    _temporary = 'temporary'
    _persistent = 'persistent'

    __persistent_path = None
    __temporary_path = None

    def __init__(self, data_dir):
        self._data_dir = data_dir

        temp_dir = os.path.join(
            self._data_dir,
            self.prefix,
            self._temporary
        )
        self.__temporary_path = Path(temp_dir).resolve()
        if not self.__temporary_path.exists():
            self.__temporary_path.mkdir(parents=True)

        persistent_dir = os.path.join(
            self._data_dir,
            self.prefix,
            self._persistent,
        )
        self.__persistent_path = Path(persistent_dir).resolve()
        if not self.__persistent_path.exists():
            self.__persistent_path.mkdir(parents=True)

    @property
    def prefix(self):
        if self._prefix is None:
            raise NotImplementedError
        return self._prefix

    @prefix.setter
    def prefix(self, name):
        self._prefix = name

    @property
    def temporary(self):
        return str(self.__temporary_path)

    @property
    def persistent(self):
        return str(self.__persistent_path)
