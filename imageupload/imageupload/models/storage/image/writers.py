from imageupload.models.storage.image import image_storage
import os
from pathlib import Path
import imageio


class BaseImageWriter(object):
    """Base for all image writer classes.

    Usage:
        ```
        writer = SomeWriter(sql_image_obj)
        writer.write_all()
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
        """
        self.__identify_input()     # sets ``input_filename``
        self.__determine_input_format()     # sets ``input_format`` and ``input_reader``
        self.__find_pending_images()    # sets ``pending_sizes``
        self.__mkdir()      # creates required directories
        self.__process()    # writes or processes the pending files

    def __process(self):
        raise NotImplementedError

    def __identify_input(self):
        """Finds out which file is to be used as input source.

        Possibilities are -

            1. input can be temporary file

            2. input can be persistent file

        Whatever the possibility is, it will detect the input file and
        set ``self.input_filename`` and ``self.input_format`` accordingly.
        """
        temp_filename = os.path.join(
            image_storage.temporary,
            self.image.basename
        )
        if os.path.exists(temp_filename):
            self.input_filename = temp_filename
            return

        # So it comes from persistent directory
        pers_filename = os.path.join(
            image_storage.persistent,
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
                image_storage.persistent,
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
            image_storage.persistent,
            self.image.basename,
        )
        path = Path(basedir)
        path.mkdir(parents=True, exist_ok=True)


class JPEGWriter(BaseImageWriter):
    """JPEG image IO handler."""

    def __process(self):
        if self.input_format == 'JPEG':
            self.__process_jpeg()
        elif self.input_format == 'PNG':
            self.__process_png()
        elif self.input_format == 'GIF':
            self.__process_gif()

    def __process_jpeg(self):
        pass

    def __process_png(self):
        pass

    def __process_gif(self):
        pass


class GIFWriter(BaseImageWriter):
    """GIF image IO handler."""

    def __process(self):
        pass


class FFMPEGWriter(BaseImageWriter):
    """FFMPEG video IO handler for animated images."""

    def __process(self):
        pass


SUPPORTED_IMG_WRITERS = dict(
    JPEG=JPEGWriter,
    GIF=GIFWriter,
    FFMPEG=FFMPEGWriter,
)


def get_image_writer(image):
    return SUPPORTED_IMG_WRITERS[image.type](image)
