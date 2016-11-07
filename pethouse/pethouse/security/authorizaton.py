class BaseAuth(object):

    def __init__(self, request):
        self.request = request

    def __acl__(self):
        raise NotImplementedError('ACL not defined!')
