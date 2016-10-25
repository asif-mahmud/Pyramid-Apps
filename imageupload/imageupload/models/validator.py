class BaseValidator(object):

    def validate(self, *args, **kwargs):
        raise NotImplementedError('Validator not implemented!')


class ValidationStatus(object):

    def __init__(self,
                 success=True,
                 msg_stack=list()):
        self._success = success
        self._msg_stack = msg_stack

    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, status):
        if isinstance(status, bool):
            self._success = status

    @property
    def msg_stack(self):
        return self._msg_stack

    @msg_stack.setter
    def msg_stack(self, msg):
        if isinstance(msg, str):
            self._msg_stack.append(msg)

    def clear(self):
        self._msg_stack.clear()
