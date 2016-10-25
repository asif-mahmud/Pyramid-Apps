from pyramid.view import forbidden_view_config


@forbidden_view_config(renderer='templates/403.jinja2')
def forbidden(request):
    return dict()
