from .base import (
    BaseValidator,
    ImageValidatorStatus,
)
import imageio


class GIFValidator(BaseValidator):
    """Validates ``GIF`` single frame or animation."""

    def validate(self):
        vstatus = ImageValidatorStatus()
        try:
            reader = imageio.get_reader(self._temp_filename)
            if reader.format.name == 'GIF':
                if reader.get_length() >= 1:
                    frame = reader.get_data(0)
                    vstatus.size = (
                        frame.shape[1],     # it's a numpy array so width, height == height, width
                        frame.shape[0]
                    )
                    if reader.get_length() == 1:    # it's a single frame GIF
                        vstatus.type = 'JPEG'
                        vstatus.extension = 'jpg'
                    else:
                        vstatus.type = 'FFMPEG'
                        vstatus.extension = 'mp4'
            reader.close()
        except Exception:
            return None
        if vstatus.type is None:
            return None
        return vstatus
