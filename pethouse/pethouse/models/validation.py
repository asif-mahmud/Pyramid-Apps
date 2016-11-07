class ValidationStatus(object):

    def __init__(self, status=False, msg=''):
        self._status = status
        self._msg_stack = list(
            msg,
        )

    @property
    def success(self):
        return self._status

    @success.setter
    def success(self, v):
        self._status = v

    @property
    def msg_stack(self):
        return self._msg_stack

    @msg_stack.setter
    def msg_stack(self, v):
        if isinstance(v, str):
            self._msg_stack.append(v)

    def error(self, msg):
        self.success = False
        self.msg_stack = msg

    def __json__(self, request):
        return dict(
            success=self.success,
            msg_stack=self.msg_stack,
        )
