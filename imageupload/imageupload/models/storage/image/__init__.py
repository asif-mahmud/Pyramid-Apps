from . import globalvars
from .. import BaseStorageInfo
from .base import (
    BaseImage,
    register_listeners,
)


class ImageStorageInfo(BaseStorageInfo):
    """Storage Info provider for images."""

    _prefix = 'images'


def includeme(config):
    settings = config.get_settings()
    globalvars.image_storage = ImageStorageInfo(settings['storage.image_dir'])
    config.add_static_view('images', globalvars.image_storage.persistent, cache_max_age=3600)
    register_listeners()
