from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('pyramid_jinja2')
    config.include('.security')
    config.include('.models')
    config.include('.routes')
    config.include('.models.storage.image')
    config.scan()
    return config.make_wsgi_app()
