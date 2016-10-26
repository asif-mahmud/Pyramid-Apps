from .security import ProfileAuth


def includeme(config):
    config.add_route(
        'show_profile',
        '/{id}',
        factory=ProfileAuth.show_profile
    )
    config.add_route(
        'add_profile_picture',
        '/add/pp',
        factory=ProfileAuth.add_profile_picture
    )
