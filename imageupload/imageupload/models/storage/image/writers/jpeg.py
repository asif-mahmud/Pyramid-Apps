from .base import BaseImageWriter
import imageio
import cv2


class JPEGWriter(BaseImageWriter):
    """JPEG image IO handler."""

    def process(self):
        if self.input_format == 'JPEG':
            self.__process_jpeg()
        elif self.input_format == 'PNG':
            self.__process_png()
        elif self.input_format == 'GIF':
            self.__process_gif()

    def __process_jpeg(self):
        for size in self.pending_sizes:
            output_filename = self.get_output_filename(size)
            writer = imageio.get_writer(
                output_filename,
                format='JPEG',
                quality=75,
            )
            frame = self.input_reader.get_data(0)
            if size != self.max_size:
                frame = cv2.resize(frame, size)
            writer.append_data(frame)
            writer.close()

    def __process_png(self):
        for size in self.pending_sizes:
            output_filename = self.get_output_filename(size)
            writer = imageio.get_writer(
                output_filename,
                format='JPEG',
                quality=75,
            )
            frame = self.input_reader.get_data(0)
            frame[~frame.any(axis=2)] = 255     # make the transparent areas white
            if size != self.max_size:
                frame = cv2.resize(frame, size)
            writer.append_data(frame[:, :, :3])     # only RGB values are valid
            writer.close()

    def __process_gif(self):
        for size in self.pending_sizes:
            output_filename = self.get_output_filename(size)
            writer = imageio.get_writer(
                output_filename,
                format='JPEG',
                quality=75,
            )
            frame = self.input_reader.get_data(0)
            frame[~frame.any(axis=2)] = 255  # make the transparent areas white
            if size != self.max_size:
                frame = cv2.resize(frame, size)
            writer.append_data(frame[:, :, :3])     # only RGB values are valid
            writer.close()
