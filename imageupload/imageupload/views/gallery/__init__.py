from .security import GalleryAuth


def includeme(config):
    config.add_route('add_gallery', '/add', factory=GalleryAuth.show_add_gallery)
    config.add_route('show_gallery', '/show/{id}', factory=GalleryAuth.show_add_gallery)
    config.add_route('edit_gallery', '/edit/{id}', factory=GalleryAuth.edit_delete_gallery)
    config.add_route('delete_gallery', '/delete/{id}',  factory=GalleryAuth.edit_delete_gallery)
    config.add_route('upload_photos', '/upload/photos', factory=GalleryAuth.edit_delete_gallery)
