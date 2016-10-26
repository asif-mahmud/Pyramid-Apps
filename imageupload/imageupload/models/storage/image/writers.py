from . import globalvars
import imageio
import cv2
import os
import sys
from pathlib import Path
import shutil


class BaseImageWriter(object):
    """Base for all image writer classes.

    Usage:
        ```
        writer = SomeWriter(sql_image_obj)
        writer.write_all()
        writer.clean_up()
        writer.delete_all()
        ```
    """

    def __init__(self, image):
        self.image = image

    def write_all(self):
        """It is a sequential job.

        The sequence is -

            1. identify input source

            2. determine input format

            3. find pending image sizes

            4. create necessary directories

            5. process files

            6. clean up
        """
        self.__identify_input()     # sets ``input_filename``
        self.__determine_input_format()     # sets ``input_format`` and ``input_reader``
        self.__find_pending_images()    # sets ``pending_sizes``
        self.__mkdir()      # creates required directories
        self.process()    # writes or processes the pending files
        self.__clean_temporary()    # clean temporary file

    def process(self):
        raise NotImplementedError

    def __identify_input(self):
        """Finds out which file is to be used as input source.

        Possibilities are -

            1. input can be temporary file

            2. input can be persistent file

        Whatever the possibility is, it will detect the input file and
        set ``self.input_filename`` and ``self.input_format`` and
        ``self.max_size`` accordingly.
        """
        temp_filename = os.path.join(
            globalvars.image_storage.temporary,
            self.image.basename
        )
        if os.path.exists(temp_filename):
            self.input_filename = temp_filename
            self.max_size = self.image.max_size
            return

        # So it comes from persistent directory
        pers_filename = os.path.join(
            globalvars.image_storage.persistent,
            self.image.basename,
            '{}x{}.{}'.format(
                self.image.available_sizes[0][0],
                self.image.available_sizes[0][1],
                self.image.extension
            )
        )
        if not os.path.exists(pers_filename):
            raise OSError
        self.input_filename = pers_filename
        self.max_size = self.image.max_size

    def __determine_input_format(self):
        """Determine the input file format.

        After this method ``self.input_format`` and
        ``self.input_reader`` will be assigned for further use.
        """
        self.input_reader = imageio.get_reader(self.input_filename)
        self.input_format = self.input_reader.format.name

    def __find_pending_images(self):
        """Find out which files are to be precessed or written to.

        These are the non-existent sizes from the ``available_sizes`` property
        of ``self.image``. After this method ``self.pending_sizes`` will contain
        the pending image sizes to be written or processed or created.
        """
        self.pending_sizes = list()
        for size in self.image.available_sizes:
            filename = os.path.join(
                globalvars.image_storage.persistent,
                self.image.basename,
                '{}x{}.{}'.format(
                    size[0],
                    size[1],
                    self.image.extension
                )
            )
            if not os.path.exists(filename):
                self.pending_sizes.append(size)

    def __mkdir(self):
        """Create the required directory structure under ``persistent`` folder.

        The required structure is like -
            ``persistent_path/basename/image_size.extension``
        """
        basedir = os.path.join(
            globalvars.image_storage.persistent,
            self.image.basename,
        )
        path = Path(basedir)
        path.mkdir(parents=True, exist_ok=True)

    def get_output_filename(self, size):
        return os.path.join(
            globalvars.image_storage.persistent,
            self.image.basename,
            '{}x{}.{}'.format(
                size[0],
                size[1],
                self.image.extension
            )
        )

    def __clean_temporary(self):
        temp_filename = os.path.join(
            globalvars.image_storage.temporary,
            self.image.basename
        )
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

    def clean_up(self):
        self.__clean_temporary()

    def delete_all(self):
        base_dir = os.path.join(
            globalvars.image_storage.persistent,
            self.image.basename,
        )
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)


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
            resize_flag = (self.max_size == size)
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
            resize_flag = (self.max_size == size)
            for frame in self.input_reader:
                if resize_flag:
                    frame = cv2.resize(frame, size)
                writer.append_data(frame)
            writer.close()
