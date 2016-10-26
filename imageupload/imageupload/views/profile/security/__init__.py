from imageupload.security.authorizaton import BaseAuth
from pyramid.security import (
    Allow,
    Authenticated,
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
                return [
                    (Allow, str(request.user.id), 'add_profile_picture'),
                ]
        return AddPP(request)
