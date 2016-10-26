from .base import (
    BaseValidator,
    ImageValidatorStatus,
)
import imageio


class JPEGValidator(BaseValidator):
    """Validates ``JPEG`` format."""

    def validate(self):
        vstatus = ImageValidatorStatus()
        try:
            reader = imageio.get_reader(self._temp_filename)
            if reader.format.name == 'JPEG':
                if reader.get_length() == 1:
                    frame = reader.get_data(0)
                    vstatus.size = (
                        frame.shape[1],  # it's a numpy array so width, height == height, width
                        frame.shape[0]
                    )
                    vstatus.extension = 'jpg'
                    vstatus.type = 'JPEG'
            reader.close()
        except Exception:
            return None
        if vstatus.size is None:
            return None
        return vstatus
