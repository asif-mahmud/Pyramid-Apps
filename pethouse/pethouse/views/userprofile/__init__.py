def includeme(config):
    config.add_route('show_profile', '/{id}')
    config.add_route('get_pets', '/{id}/pets')
    config.add_route('add_pet', '/add/pet')
