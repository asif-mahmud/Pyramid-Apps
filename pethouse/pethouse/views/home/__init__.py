def includeme(config):
    config.add_route('home', '/')
    config.add_route('register', '/register')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
