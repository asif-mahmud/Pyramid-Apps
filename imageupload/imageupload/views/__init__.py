def includeme(config):
    config.add_route('home_redirect', '/')
    config.include('.home', route_prefix='home')
    config.include('.profile', route_prefix='profile')
