from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from imageupload.views.home.security import HomeAuth


@view_config(route_name='home_redirect')
def home_redirect(request):
    return HTTPFound(
        location=request.route_url('home')
    )


def includeme(config):
    config.add_route('home', '/', factory=HomeAuth.home)
    config.add_route('login', '/login', factory=HomeAuth.home)
    config.add_route('logout', '/logout', factory=HomeAuth.home)
    config.add_route('register', '/register', factory=HomeAuth.home)
