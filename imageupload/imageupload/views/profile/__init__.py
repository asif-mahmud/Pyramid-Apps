from .security import ProfileAuth


def includeme(config):
    config.add_route(
        'add_profile_picture',
        '/pp',
        factory=ProfileAuth.add_profile_picture
    )
    config.add_route(
        'show_profile',
        '/{id}',
        factory=ProfileAuth.show_profile
    )
