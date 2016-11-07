from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pethouse.models.user import User
from pethouse.models.validation import ValidationStatus
from pethouse.models.validation import ValidationStatus
from pethouse.models.user import User
from pyramid.security import (
    remember,
    forget,
)


class HomeView(object):

    def __init__(self, request):
        self.request = request

    @view_config(route_name='home',
                 renderer='../templates/home.jinja2')
    def landing_page(self):
        return dict()

    @view_config(route_name='register',
                 renderer='json',
                 request_method='POST')
    def register(self):
        user = User(
            username=self.request.json_body['username'],
            first_name=self.request.json_body['first_name'],
            last_name=self.request.json_body['last_name'],
        )
        vstatus = user.validate(password=self.request.json_body['password'],
                                password_retype=self.request.json_body['password_retype'])
        if vstatus.success:
            user.set_password(self.request.json_body['password'])
            self.request.dbsession.add(user)
            return dict(
                success=True,
                msg_stack=[
                    'Registration was successful.',
                    'Now you can login.'
                ]
            )
        return vstatus

    @view_config(route_name='login',
                 renderer='../templates/home.jinja2')
    def login(self):
        if 'login.submitted' in self.request.params:
            username = self.request.POST['username']
            password = self.request.POST['password']
            user = self.request.dbsession.query(
                User
            ).filter_by(
                username=username
            ).first()
            if user is not None:
                if not user.check_password(password):
                    return dict(
                        error='Username or password is wrong.'
                    )
            else:
                return dict(
                    error='User not found.'
                )
            headers = remember(self.request, user.id)
            return HTTPFound(
                location=self.request.route_url('show_profile', id=user.id),
                headers=headers,
            )
        return dict()

    @view_config(route_name='logout')
    def logout(self):
        headers = forget(self.request)
        return HTTPFound(
            location=self.request.route_url('home'),
            headers=headers,
        )
