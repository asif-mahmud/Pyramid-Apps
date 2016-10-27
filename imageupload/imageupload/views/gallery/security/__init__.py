from imageupload.security.authorizaton import BaseAuth
from pyramid.security import (
    Allow,
    Authenticated,
    DENY_ALL,
)


class GalleryAuth(object):

    @staticmethod
    def show_add_gallery(request):
        class AuthAddGallery(BaseAuth):

            def __acl__(self):
                return [
                    (Allow, Authenticated, 'add_gallery'),
                    (Allow, Authenticated, 'show_gallery'),
                ]
        return AuthAddGallery(request)

    @staticmethod
    def edit_delete_gallery(request):
        class AuthDeleteGallery(BaseAuth):

            def __acl__(self):
                if self.request.user is not None:
                    return [
                        (Allow, str(self.request.user.id), 'delete_gallery'),
                        (Allow, str(self.request.user.id), 'edit_gallery'),
                        (Allow, str(self.request.user.id), 'upload_photos'),
                    ]
                else:
                    return [
                        DENY_ALL,
                    ]
        return AuthDeleteGallery(request)
