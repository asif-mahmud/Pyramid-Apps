from .base import BaseImageWriter
import imageio
import cv2


class GIFWriter(BaseImageWriter):
    """GIF image IO handler."""

    def process(self):
        if self.input_format == 'PNG':
            self.__process_png()
        elif self.input_format == 'GIF':
            self.__process_gif()

    def __process_png(self):
        for size in self.pending_sizes:
            output_filename = self.get_output_filename(size)
            writer = imageio.get_writer(
                output_filename,
                format='GIF',
            )
            frame = self.input_reader.get_data(0)
            if size != self.max_size:
                frame = cv2.resize(frame, size)
            writer.append_data(frame)
            writer.close()

    def __process_gif(self):
        for size in self.pending_sizes:
            output_filename = self.get_output_filename(size)
            writer = imageio.get_writer(
                output_filename,
                format='GIF',
            )
            frame = self.input_reader.get_data(0)   # it's a single frame image
            if size != self.max_size:
                frame = cv2.resize(frame, size)
            writer.append_data(frame)
            writer.close()
