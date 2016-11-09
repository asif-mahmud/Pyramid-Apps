from pyramid.view import view_config
from pethouse.models.user import User
from pethouse.models.pets import Pet
from pethouse.models.pet_types import PetType
from pethouse.models.validation import ValidationStatus
from pyramid.httpexceptions import HTTPNotFound


class UserProfile(object):

    def __init__(self, request):
        self.request = request

    @view_config(route_name='show_profile',
                 renderer='../templates/show_profile.jinja2')
    def show_profile(self):
        user = self.request.dbsession.query(
            User
        ).filter_by(
            id=self.request.matchdict['id']
        ).first()
        if user is None:
            return HTTPNotFound()
        return dict(
            user=user,
        )

    @view_config(route_name='add_pet',
                 request_method='POST',
                 renderer='json')
    def add_pet(self):
        vstatus = ValidationStatus()
        name = self.request.json_body['name']
        description = self.request.json_body['description']
        type_id = self.request.json_body['type']
        if len(name) == 0 or \
            len(description) == 0:
            vstatus.error('Name or description can not be empty!')
            return dict(
                status=vstatus
            )
        pet_type = self.request.dbsession.query(PetType).filter_by(
            id=type_id
        ).first()
        owner = self.request.user
        pet = Pet(
            name=name,
            description=description,
        )
        pet.type = pet_type
        pet.owner = owner
        self.request.dbsession.add(pet)
        vstatus.success = True
        vstatus.msg_stack = 'Pet has been added.'
        return dict(
            status=vstatus,
            pet=pet
        )

    @view_config(route_name='get_pets',
                 request_method='GET',
                 renderer='json')
    def get_pets(self):
        user = self.request.dbsession.query(User).filter_by(
            id=self.request.matchdict['id']
        ).first()
        return dict(
            pets=user.pets,
        )
