from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from ..models import (
    Blogger,
    Blog
)
from pyramid.security import (
    remember,
    forget,
)
from sqlalchemy import desc
from pyramid.security import Authenticated


class Home(object):

    def __init__(self, request):
        self.request = request

    @view_config(route_name='home',
                 renderer='../templates/pages/home.jinja2',
                 permission='view')
    def login_or_reg(self):
        return dict()

    @view_config(route_name='home',
                 renderer='../templates/pages/home.jinja2',
                 effective_principals=[Authenticated,])
    def home_view(self):
        blogs = self.request.dbsession.query(Blog).order_by(desc(
            Blog.updated_on)).limit(5).all()
        return dict(
            blogs=blogs,
        )

    @view_config(route_name='login',
                 renderer='../templates/pages/home.jinja2',
                 permission='view')
    def login(self):
        if 'login.submitted' in self.request.params:
            name = self.request.params['name']
            password = self.request.params['password']
            if len(name) < 4 or len(password) < 6:
                return dict(
                    login_error_msg='Not enough data!',
                    login_name=name,
                )
            blogger = self.request.dbsession.query(Blogger).filter_by(
                name=name,
            ).first()
            if not blogger:
                return dict(
                    login_error_msg='Username not found!',
                    login_name=name,
                )
            if not blogger.check_password(password):
                return dict(
                    login_error_msg='Wrong password!',
                    login_name=name,
                )

            headers = remember(self.request, blogger.id)
            return HTTPFound(
                location=self.request.route_url('home'),
                headers=headers,
            )
        return dict()

    @view_config(route_name='logout')
    def logout(self):
        if self.request.user:
            headers = forget(self.request)
            return HTTPFound(
                location=self.request.route_url('home'),
                headers=headers,
            )
        return dict()

    @view_config(route_name='register',
                 renderer='../templates/pages/home.jinja2',
                 permission='view')
    def register(self):
        if 'reg.submitted' in self.request.params:
            name = self.request.params['name']
            password = self.request.params['password']
            password_retype = self.request.params['password-retype']
            if len(name) < 4 or len(password) < 6 or len(password_retype) < 6:
                return dict(
                    reg_error_msg='Name or password too short!',
                    reg_name=name,
                )
            if password != password_retype:
                return dict(
                    reg_error_msg='Password did not match!',
                    reg_name=name,
                )
            if self.request.dbsession.query(Blogger).filter_by(
                name=name
            ).first() is not None:
                return dict(
                    reg_error_msg='Username already taken!',
                    reg_name=name,
                )

            blogger = Blogger(name=name)
            blogger.set_password(password)
            self.request.dbsession.add(blogger)

            return dict(
                reg_error_msg='Registration was successful. You can now login to'
                              ' your profile',
                reg_name=None,
            )
        return dict()
