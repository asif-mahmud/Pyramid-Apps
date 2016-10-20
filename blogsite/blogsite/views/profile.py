from pyramid.view import view_config
from ..models import Blogger
from pyramid.httpexceptions import HTTPNotFound


class Profile(object):

    def __init__(self, request):
        self.request = request

    @view_config(route_name='show_profile',
                 renderer='../templates/pages/show_profile.jinja2',
                 permission='view_profile')
    def show_profile(self):
        """Show a ``blogger's`` profile.

        Url Params:
            pid(int): Profile ``id`` of a ``blogger``.

        Notes: Anyone logged in should be able to visit anyone's profile.
        """
        profile_id = self.request.matchdict['pid']
        blogger = self.request.dbsession.query(Blogger).filter_by(
            id=profile_id,
        ).first()
        if not blogger:
            return HTTPNotFound(detail='Sorry the profile is not found!')
        return dict(
            blogger=blogger,
        )

    @view_config(route_name='edit_profile',
                 renderer='../templates/pages/edit_profile.jinja2',
                 permission='edit_profile')
    def edit_profile(self):
        """Only the respective ``blogger`` will be able to edit his profile.

        Url Params:
            pid(int): Profile ``id`` of a ``blogger``.
        """
        profile_id = self.request.matchdict['pid']
        blogger = self.request.dbsession.query(Blogger).filter_by(
            id=profile_id,
        ).first()
        if not blogger:
            return HTTPNotFound(detail='Sorry the profile is not found!')
        if 'edit.submitted' in self.request.params:
            name = self.request.params['name']
            new_password = self.request.params['new-password']
            new_password_retype = self.request.params['new-password-retype']
            old_password = self.request.params['old-password']
            if not blogger.check_password(old_password):
                return dict(
                    error_msg='Wrong password!',
                    name=name,
                )
            if name != blogger.name:
                if len(name) < 4:
                    return dict(
                        error_msg='Username must be at least 4 characters long!',
                        name=name,
                    )
                profile_check = self.request.dbsession.query(Blogger).filter_by(
                    name=name,
                ).first()
                if profile_check is not None:
                    return dict(
                        error_msg='Profile name already exists!',
                        name=blogger.name,
                    )
                blogger.name = name
            if len(new_password) > 0:
                if len(new_password) < 6:
                    return dict(
                        error_msg='Password too short!',
                        name=name,
                    )
                if new_password != new_password_retype:
                    return dict(
                        error_msg='New password did not match!',
                        name=name,
                    )
                blogger.set_password(new_password)
            return dict(
                error_msg='Profile updated!',
                name=blogger.name,
            )
        return dict(
            name=blogger.name
        )

