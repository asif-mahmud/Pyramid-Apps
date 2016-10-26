from .base import (
    BaseValidator,
    ImageValidatorStatus,
)
import imageio
import numpy as np


class PNGValidator(BaseValidator):
    """Validator for ``PNG`` type images."""

    def validate(self):
        vstatus = ImageValidatorStatus()
        try:
            reader = imageio.get_reader(self._temp_filename)
            if reader.format.name == 'PNG':
                if reader.get_length() == 1:
                    frame = reader.get_data(0)
                    vstatus.size = (
                        frame.shape[1],  # it's a numpy array so width, height == height, width
                        frame.shape[0]
                    )
                    if not np.all(frame.any(axis=2)):
                        vstatus.type = 'JPEG'
                        vstatus.extension = 'jpg'
                    else:
                        vstatus.type = 'GIF'
                        vstatus.extension = 'gif'
            reader.close()
        except Exception:
            return None
        if vstatus.type is None:
            return None
        return vstatus
