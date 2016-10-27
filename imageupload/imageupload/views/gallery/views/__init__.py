from pyramid.view import view_config
from imageupload.models.gallery import (
    Gallery,
    GalleryImage,
)
from pyramid.httpexceptions import HTTPFound


class GalleryView(object):

    def __init__(self, request):
        self.request = request

    @view_config(route_name='add_gallery',
                 renderer='../templates/add_gallery.jinja2',
                 permission='add_gallery')
    def add_gallery(self):
        if 'form.submitted' in self.request.params:
            title = self.request.params['title']
            desc = self.request.params['description']
            gallery = Gallery(title=title, description=desc)
            vstatus = gallery.validate()
            if not vstatus.success:
                return dict(
                    error_msg=vstatus.msg_stack,
                    title=title,
                    description=desc,
                )
            gallery.user = self.request.user
            self.request.dbsession.add(gallery)
            return HTTPFound(
                location=self.request.route_url('show_profile', id=self.request.user.id)
            )
        return dict()

    @view_config(route_name='delete_gallery',
                 permission='delete_gallery')
    def delete_gallery(self):
        id = self.request.matchdict['id']
        gallery = self.request.dbsession.query(
            Gallery
        ).filter_by(
            id=id,
        ).first()
        self.request.dbsession.delete(gallery)
        return HTTPFound(
            location=self.request.route_url('show_profile', id=self.request.user.id)
        )

    @view_config(route_name='edit_gallery',
                 renderer='../templates/edit_gallery.jinja2',
                 permission='edit_gallery')
    def edit_gallery(self):
        gallery = self.request.dbsession.query(
            Gallery,
        ).filter_by(
            id=self.request.matchdict['id'],
        ).first()
        if 'form.submitted' in self.request.params:
            vstatus = gallery.validate(
                title=self.request.params['title'],
                description=self.request.params['description'],
            )
            if not vstatus.success:
                return dict(
                    error_msg=vstatus.msg_stack,
                    gallery=gallery,
                )
            gallery.title = self.request.params['title']
            gallery.description = self.request.params['description']
            return HTTPFound(
                location=self.request.route_url('show_profile', id=self.request.user.id)
            )
        return dict(
            gallery=gallery,
        )

    @view_config(route_name='show_gallery',
                 renderer='../templates/show_gallery.jinja2',
                 permission='show_gallery')
    def show_gallery(self):
        id = self.request.matchdict['id']
        gallery = self.request.dbsession.query(
            Gallery
        ).filter_by(
            id=id,
        ).first()
        return dict(
            gallery=gallery,
        )

    @view_config(route_name='upload_photos',
                 permission='upload_photos',
                 renderer='../templates/upload_photos.jinja2')
    def upload_photos(self):
        if 'form.submitted' in self.request.params:
            files = self.request.POST.getall('files')
            gallery = self.request.dbsession.query(
                Gallery,
            ).filter_by(
                id=self.request.matchdict['id'],
            ).first()
            if gallery is None:
                return dict()
            for img in files:
                try:
                    img.file
                except AttributeError:
                    continue
                g_img = GalleryImage()
                check = g_img.from_file_obj(img.file)
                if check is None:
                    continue
                g_img.gallery = gallery
                self.request.dbsession.add(g_img)
            return HTTPFound(
                location=self.request.route_url(
                    'show_gallery',
                    id=self.request.matchdict['id'],
                )
            )
        return dict()

