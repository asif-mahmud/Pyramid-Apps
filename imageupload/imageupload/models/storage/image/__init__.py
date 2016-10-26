from . import globalvars
from .. import BaseStorageInfo
from .base import (
    BaseImageQuery,
    BaseImage,
)
from sqlalchemy.event import listen
from sqlalchemy.orm import Session


class ImageStorageInfo(BaseStorageInfo):
    """Storage Info provider for images."""

    _prefix = 'images'


def includeme(config):
    settings = config.get_settings()
    globalvars.image_storage = ImageStorageInfo(settings['storage.image_dir'])
    config.add_static_view('images', globalvars.image_storage.persistent, cache_max_age=3600)

    listen(BaseImage, 'after_insert', BaseImageQuery.after_insert, propagate=True)
    listen(BaseImage, 'after_delete', BaseImageQuery.after_delete, propagate=True)
    listen(Session, 'after_soft_rollback', BaseImageQuery.after_soft_rollback)
    listen(Session, 'after_commit', BaseImageQuery.after_commit)
