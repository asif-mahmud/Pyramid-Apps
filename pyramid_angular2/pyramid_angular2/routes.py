def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('node_modules', 'node_modules', cache_max_age=3600)
    config.add_static_view('ngapp', 'ngapp', cache_max_age=3600)
    config.add_route('home', '/')
