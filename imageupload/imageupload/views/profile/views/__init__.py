from pyramid.view import view_config
from imageupload.models import User, ProfilePicture
from pyramid.httpexceptions import HTTPFound


class UserProfile(object):

    def __init__(self, request):
        self.request = request

    @view_config(route_name='show_profile',
                 renderer='../templates/show_profile.jinja2',
                 permission='view_profile')
    def show_profile(self):
        pid = int(self.request.matchdict['id'])
        if self.request.user.id == pid:
            return dict(
                user=self.request.user,
            )
        user = self.request.dbsession.query(
            User
        ).filter_by(
            id=pid
        ).first()
        return dict(
            user=user,
        )

    @view_config(route_name='add_profile_picture',
                 renderer='../templates/add_profile_picture.jinja2',
                 permission='add_profile_picture')
    def add_profile_picture(self):
        if 'form.submitted' in self.request.params:
            img = ProfilePicture()
            check = img.from_file_obj(self.request.POST['file'].file)
            if check is None:
                return dict()
            img.add_thumbnail((128, 128))
            if self.request.user.profile_picture:
                del self.request.user.profile_picture
            self.request.user.profile_picture = img
            self.request.dbsession.add(img)
            return HTTPFound(
                location=self.request.route_url(
                    'show_profile',
                    id=self.request.user.id,
                )
            )
        return dict()
