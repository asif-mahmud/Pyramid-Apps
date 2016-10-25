from imageupload.models.storage import BaseStorageInfo


class ImageStorageInfo(BaseStorageInfo):
    """Storage Info provider for images."""

    _prefix = 'images'


"""This may be the single most important variable for the image storage."""
image_storage = None


def includeme(config):
    global image_storage
    settings = config.get_settings()
    image_storage = ImageStorageInfo(settings['storage.image_dir'])
    config.add_static_view('images', image_storage.persistent, cache_max_age=3600)
