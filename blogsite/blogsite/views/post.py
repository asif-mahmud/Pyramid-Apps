from pyramid.view import view_config
from ..models import (
    Blog,
    Blogger,
    Post,
)
from sqlalchemy import desc


class PostView(object):

    def __init__(self, request):
        self.request = request

    @view_config(route_name='add_post',
                 renderer='../templates/pages/add_post.jinja2',
                 permission='add_post')
    def add_post(self):
        return dict()

    @view_config(route_name='edit_post',
                 renderer='../templates/pages/add_post.jinja2',
                 permission='edit_post')
    def edit_post(self):
        """Edit an existing ``Post``.

        Url Param:
            pid(int): Post ``id``
        """
        return dict()

    @view_config(route_name='show_post',
                 renderer='../templates/pages/show_post.jinja2',
                 permission='show_posts')
    def show_post(self):
        """Show a ``Post``.

        Url Param:
            pid(int): Post ``id``
        """
        return dict()

    @view_config(route_name='show_all_posts',
                 renderer='../templates/pages/show_all_posts.jinja2',
                 permission='show_posts')
    def show_all_posts(self):
        posts = self.request.dbsession.query(Post).order_by(desc(
            Post.updated_on
        )).all()
        return dict(
            posts=posts,
        )
