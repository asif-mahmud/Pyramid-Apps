from .authentication import BlogSiteAuthPolicy, get_user
from pyramid.authorization import ACLAuthorizationPolicy


def includeme(config):
    settings = config.get_settings()

    auth_policy = BlogSiteAuthPolicy(
        settings['auth.secret'],
    )

    config.set_authentication_policy(auth_policy)
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.add_request_method(get_user, 'user', reify=True)
