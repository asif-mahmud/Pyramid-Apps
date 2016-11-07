from pyramid.view import view_config
from pethouse.models.user import User
from pyramid.httpexceptions import HTTPNotFound


class UserProfile(object):

    def __init__(self, request):
        self.request = request

    @view_config(route_name='show_profile',
                 renderer='../templates/show_profile.jinja2')
    def show_profile(self):
        user = self.request.dbsession.query(
            User
        ).filter_by(
            id=self.request.matchdict['id']
        ).first()
        if user is None:
            return HTTPNotFound()
        return dict(
            user=user,
        )
