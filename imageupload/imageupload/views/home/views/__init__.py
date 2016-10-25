from pyramid.view import view_config
from imageupload.models import User
from pyramid.security import (
    remember,
    forget,
)
from pyramid.httpexceptions import HTTPFound


class HomeView(object):

    def __init__(self, request):
        self.request = request

    @view_config(route_name='home',
                 renderer='../templates/home.jinja2',
                 permission='view')
    def home(self):
        return dict()

    @view_config(route_name='login',
                 renderer='../templates/home.jinja2',
                 permission='view')
    def login(self):
        if 'login.submitted' in self.request.params:
            name = self.request.params['name']
            password = self.request.params['password']
            user = self.request.dbsession.query(User).filter_by(
                name=name,
            ).first()
            if not user:
                return dict(
                    login_error_msg='Username was not found!',
                    login_name=name,
                )
            vstatus = user.validate(
                None,
                password=password,
                check_password=True,
            )
            if not vstatus.success:
                return dict(
                    login_error_msg=vstatus.msg_stack,
                    login_name=name,
                )
            headers = remember(self.request, user.id)
            return HTTPFound(
                location=self.request.route_url('home'),
                headers=headers,
            )
        return dict()

    @view_config(route_name='logout',
                 permission='view')
    def logout(self):
        headers = forget(self.request)
        return HTTPFound(
            location=self.request.route_url('home'),
            headers=headers,
        )

    @view_config(route_name='register',
                 renderer='../templates/home.jinja2',
                 permission='view')
    def register(self):
        if 'reg.submitted' in self.request.params:
            name = self.request.params['name']
            password = self.request.params['password']
            password_retype = self.request.params['password-retype']
            user = User(name=name)
            vstatus = user.validate(self.request.dbsession,
                                   password=password,
                                   password_check=password_retype)
            if not vstatus.success:
                return dict(
                    reg_error_msg=vstatus.msg_stack,
                    reg_name=name,
                )
            user.set_password(password)
            self.request.dbsession.add(user)
            return dict(
                reg_error_msg='Registration was successful!'
            )
        return dict()
