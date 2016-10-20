from pyramid.view import view_config
from ..models import (
    Blog,
    Blogger,
)
from pyramid.httpexceptions import HTTPFound
from sqlalchemy import desc


class BlogView(object):

    def __init__(self, request):
        self.request = request

    @view_config(route_name='add_blog',
                 renderer='../templates/pages/add_blog.jinja2',
                 permission='add_blog')
    def add_blog(self):
        if 'blog.submitted' in self.request.params:
            title = self.request.params['title']
            description = self.request.params['description']
            if not len(title) > 0 or not len(description) > 0:
                return dict(
                    error_msg='Title or description must not be empty.'
                )
            if self.request.dbsession.query(Blog).filter_by(
                title=title,
            ).first():
                return dict(
                    error_msg='Title is already taken!',
                )
            blog = Blog(title=title, description=description)
            blog.blogger_id = self.request.user.id
            self.request.dbsession.add(blog)

            return HTTPFound(
                location=self.request.route_url('home'),
            )
        return dict()

    @view_config(route_name='edit_blog',
                 renderer='../templates/pages/add_blog.jinja2',
                 permission='edit_blog')
    def edit_blog(self):
        """Edit an existing ``blog``.

        Url Params:
            bid(int): ``id`` of the ``blog`` to edit.
        """
        blog_id = self.request.matchdict['bid']
        blog = self.request.dbsession.query(Blog).filter_by(
            id=blog_id,
        ).first()
        if 'blog.submitted' in self.request.params:
            title = self.request.params['title']
            description = self.request.params['description']
            if not len(title) > 0 or not len(description) > 0:
                return dict(
                    blog=blog,
                    error_msg='Title or description must not be empty.'
                )
            if title != blog.title:
                if self.request.dbsession.query(Blog).filter_by(
                        title=title,
                ).first():
                    return dict(
                        blog=blog,
                        error_msg='Title is already taken!',
                    )
                blog.title = title
            if description != blog.description:
                blog.description = description
            return HTTPFound(
                location=self.request.route_url('home'),
            )
        return dict(
            blog=blog,
        )

    @view_config(route_name='show_blog',
                 renderer='../templates/pages/show_blog.jinja2',
                 permission='show_blog')
    def show_blog(self):
        """Visit a ``blog``.

        Url Params:
            bid(int): ``id`` of the ``blog`` to visit.
        """
        blog_id = self.request.matchdict['bid']
        blog = self.request.dbsession.query(Blog).filter_by(
            id=blog_id,
        ).first()
        return dict(
            blog=blog,
        )

    @view_config(route_name='all_blogs',
                 renderer='../templates/pages/all_blogs.jinja2',
                 permission='show_all_blogs')
    def all_blogs(self):
        return dict(
            blogs=self.request.dbsession.query(Blog).order_by(
                desc(Blog.updated_on)
            ).all()
        )
