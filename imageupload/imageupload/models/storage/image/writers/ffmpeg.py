from .base import BaseImageWriter
import imageio
import cv2
import os
import sys


class FFMPEGWriter(BaseImageWriter):
    """FFMPEG video IO handler for animated images."""

    def process(self):
        if sys.platform != 'linux':
            raise OSError('Platform not supported!')
        for path in os.environ['PATH'].split(':'):
            ffmpeg_path = os.path.join(
                path,
                'ffmpeg'
            )
            if os.path.exists(ffmpeg_path):
                os.environ['IMAGEIO_FFMPEG_EXE'] = ffmpeg_path
                break
        else:
            raise OSError('FFMPEG binary not found!')

        if self.input_format == 'GIF':
            self.__process_gif()
        elif self.input_format == 'FFMPEG':
            self.__process_ffmpeg()

    def __process_gif(self):
        input_fps = 1000/self.input_reader.get_meta_data()['ANIMATION']['FrameTime']
        for size in self.pending_sizes:
            output_filename = self.get_output_filename(size)
            writer = imageio.get_writer(
                output_filename,
                format='FFMPEG',
                ffmpeg_log_level='error',
                fps=int(input_fps),
                ffmpeg_params=[
                    '-movflags',
                    'faststart',
                ]
            )
            resize_flag = (self.max_size != size)
            for frame in self.input_reader:
                if resize_flag:
                    frame = cv2.resize(frame, size)
                writer.append_data(frame)
            writer.close()

    def __process_ffmpeg(self):
        input_fps = self.input_reader.get_meta_data()['fps']
        for size in self.pending_sizes:
            output_filename = self.get_output_filename(size)
            writer = imageio.get_writer(
                output_filename,
                format='FFMPEG',
                ffmpeg_log_level='error',
                fps=int(input_fps),
                ffmpeg_params=[
                    '-movflags',
                    'faststart',
                ]
            )
            resize_flag = (self.max_size != size)
            for frame in self.input_reader:
                if resize_flag:
                    frame = cv2.resize(frame, size)
                writer.append_data(frame)
            writer.close()
