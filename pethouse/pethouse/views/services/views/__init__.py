from pyramid.view import view_config
from pethouse.models.pet_types import PetType


@view_config(route_name='get_pet_types',
             renderer='json',
             request_method='GET')
def get_pet_types(request):
    return request.dbsession.query(PetType).all()
