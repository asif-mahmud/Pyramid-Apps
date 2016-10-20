from pyramid.security import (
    Allow,
    Deny,
    Everyone,
    Authenticated,
    DENY_ALL,
)
from ..models import (
    Blogger,
    Blog,
    Post,
)


class HomePage(object):

    def __init__(self, request):
        self.request = request

    def __acl__(self):
        return [
            (Allow, Everyone, 'view'),
        ]


class ShowProfile(object):

    def __init__(self, request):
        self.request = request

    def __acl__(self):
        return [
            (Allow, Authenticated, 'view_profile'),
            DENY_ALL,
        ]


class EditProfile(object):

    def __init__(self, request):
        self.request = request

    def __acl__(self):
        profile_id = self.request.matchdict['pid']
        profile_owner = self.request.dbsession.query(Blogger).filter_by(
            id=profile_id,
        ).first()
        return [
            (Allow, str(profile_owner.id), 'edit_profile'),
            DENY_ALL,
        ]


class AddBlog(object):

    def __init__(self, request):
        self.request = request

    def __acl__(self):
        return [
            (Allow, Authenticated, 'add_blog'),
            DENY_ALL,
        ]


class EditBlog(object):

    def __init__(self, request):
        self.request = request

    def __acl__(self):
        blog = self.request.dbsession.query(Blog).filter_by(
            id=self.request.matchdict['bid'],
        ).first()
        return [
            (Allow, str(blog.blogger_id), 'edit_blog'),
            DENY_ALL,
        ]


class ShowBlog(object):
    def __init__(self, request):
        self.request = request

    def __acl__(self):
        blog = self.request.dbsession.query(Blog).filter_by(
            id=self.request.matchdict['bid'],
        ).first()
        return [
            (Allow, str(blog.blogger_id), 'show_blog'),
            DENY_ALL,
        ]


class ShowAllBlogs(object):
    def __init__(self, request):
        self.request = request

    def __acl__(self):
        return [
            (Allow, Authenticated, 'show_all_blogs'),
            DENY_ALL,
        ]


class AuthBase(object):

    def __init__(self, request):
        self.request = request

    def __acl__(self):
        raise NotImplementedError()


class AuthPosts(object):

    @staticmethod
    def add_post(request):
        class AddPost(AuthBase):

            def __acl__(self):
                return [
                    (Allow, Authenticated, 'add_post'),
                    DENY_ALL,
                ]

        return AddPost(request)

    @staticmethod
    def edit_post(request):
        class EditPost(AuthBase):

            def __acl__(self):
                post_id = self.request.matchdict['pid']
                post = self.request.dbsession.query(Post).filter_by(
                    id=post_id
                ).first()
                return [
                    (Allow, str(post.blogger_id), 'edit_post'),
                    DENY_ALL,
                ]
        return EditPost(request)

    @staticmethod
    def show_posts(request):
        class ShowPosts(AuthBase):

            def __acl__(self):
                return [
                    (Allow, Authenticated, 'show_posts'),
                    DENY_ALL,
                ]

        return ShowPosts(request)
