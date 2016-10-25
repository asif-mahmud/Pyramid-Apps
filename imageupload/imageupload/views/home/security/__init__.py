from imageupload.security import BaseAuth
from pyramid.security import (
    DENY_ALL,
    Deny,
    Everyone,
    Allow,
)


class HomeAuth(object):

    @staticmethod
    def home(request):
        class HomePage(BaseAuth):

            def __acl__(self):
                return [
                    (Allow, Everyone, 'view'),
                ]
        return HomePage(request)
