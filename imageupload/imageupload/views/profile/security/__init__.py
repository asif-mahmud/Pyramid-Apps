from imageupload.security.authorizaton import BaseAuth
from pyramid.security import (
    Allow,
    Authenticated,
    DENY_ALL,
)


class ProfileAuth(object):

    @staticmethod
    def show_profile(request):
        class ShowProfile(BaseAuth):

            def __acl__(self):
                return [
                    (Allow, Authenticated, 'view_profile'),
                ]
        return ShowProfile(request)

    @staticmethod
    def add_profile_picture(request):
        class AddPP(BaseAuth):

            def __acl__(self):
                if self.request.user is not None:
                    return [
                        (Allow, str(request.user.id), 'add_profile_picture'),
                    ]
                else:
                    return [
                        DENY_ALL,
                    ]
        return AddPP(request)
