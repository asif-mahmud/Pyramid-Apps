from pyramid.authentication import AuthTktAuthenticationPolicy
from imageupload.models import User
from pyramid.security import (
    Everyone,
    Authenticated,
)


class BlogSiteAuthPolicy(AuthTktAuthenticationPolicy):

    def authenticated_userid(self, request):
        if request.user:
            return request.user.id

    def effective_principals(self, request):
        principals = [Everyone, ]
        if request.user:
            principals.append(str(request.user.id))
            principals.append(Authenticated)
            for role in request.user.roles:
                principals.append(role)
        return principals

def get_user(request):
    user_id = request.unauthenticated_userid
    if user_id:
        return request.dbsession.query(User).filter_by(
            id=user_id
        ).first()
