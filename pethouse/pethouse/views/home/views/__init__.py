from pyramid.view import view_config


class HomeView(object):

    def __init__(self, request):
        self.request = request

    @view_config(route_name='home',
                 renderer='../templates/home.jinja2')
    def landing_page(self):
        return dict()
