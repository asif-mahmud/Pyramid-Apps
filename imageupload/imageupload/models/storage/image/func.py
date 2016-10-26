from . import writers
from . import validators


SUPPORTED_IMG_VALIDATORS = (
    'JPEGValidator',
    'PNGValidator',
    'GIFValidator',
)


SUPPORTED_IMG_WRITERS = dict(
    JPEG='JPEGWriter',
    GIF='GIFWriter',
    FFMPEG='FFMPEGWriter',
)


def get_validator_status(temp_filename):
    for v_name in SUPPORTED_IMG_VALIDATORS:
        validator = getattr(validators, v_name)(temp_filename)
        vstatus = validator.validate()
        if vstatus is not None:
            return vstatus


def get_image_writer(image):
    try:
        WriterClass = getattr(writers, SUPPORTED_IMG_WRITERS[image.image_type])
        return WriterClass(image)
    except AttributeError:
        raise
