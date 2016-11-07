from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound


@view_config(route_name='home_redirect')
def redirect_to_home(request):
    return HTTPFound(
        location=request.route_url('home')
    )



def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('ngsrc', 'ngsrc', cache_max_age=3600)
    config.add_static_view('ngmodules', 'ngsrc/node_modules', cache_max_age=3600)
    config.add_static_view('semantic', 'ngsrc/semantic/dist', cache_max_age=3600)
    config.add_static_view('ngapps', 'ngsrc/ngapps', cache_max_age=3600)

    config.add_route('home_redirect', '/')

    # Add all of your view modules by include method
    config.include('.views.home', route_prefix='home')
    config.include('.views.userprofile', route_prefix='user')
