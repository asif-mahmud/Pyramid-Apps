class ImageValidatorStatus(object):
    """Return type of any ``validator``.

    Properties:
        size(tuple(int, int) or list(int, int)): Original/Output size

        type(str): Output codec for ``imageio``

        extension(str): Output ``extension``.
    """

    _output_size = None
    _output_type = None
    _output_extension = None

    def __init__(self,
                 original_size=None,
                 output_type=None,
                 output_extension=None):
        self._output_size = original_size
        self._output_type = output_type
        self._output_extension = output_extension

    @property
    def size(self):
        return self._output_size

    @size.setter
    def size(self, _size):
        if isinstance(_size, list) or isinstance(_size, tuple):
            self._output_size = _size

    @property
    def type(self):
        return self._output_type

    @type.setter
    def type(self, _type):
        if isinstance(_type, str):
            self._output_type = _type

    @property
    def extension(self):
        return self._output_extension

    @extension.setter
    def extension(self, _ext):
        if isinstance(_ext, str):
            self._output_extension = _ext


class BaseValidator(object):
    """Base for all validators.

    Every validator represents a specific image format. It is it's job to
    validate the incoming data and return a ``ImageValidatorStatus``
    consisting -

        1. size(list(int, int) or tuple(int, int)):
            size of the temporary image
        2. type(str):
            Codec name for ``imageio``
        3. extension(str):
            Output file extension.
    """

    def __init__(self, temp_filename):
        self._temp_filename = temp_filename

    def validate(self):
        """This method must provide an ``ImageValidatorStatus`` or ``None``."""
        raise NotImplementedError
