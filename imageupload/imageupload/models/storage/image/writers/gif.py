from .base import BaseImageWriter
import imageio
from wand.image import Image


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
            input_img = Image(filename=self.input_filename)

            if size != self.max_size:
                input_img.resize(width=size[0], height=size[1])
            input_img.convert('GIF')
            input_img.save(filename=output_filename)

    def __process_gif(self):
        for size in self.pending_sizes:
            output_filename = self.get_output_filename(size)
            input_img = Image(filename=self.input_filename)

            if size != self.max_size:
                input_img.resize(width=size[0], height=size[1])
            input_img.save(filename=output_filename)
