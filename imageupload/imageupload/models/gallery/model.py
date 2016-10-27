from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey,
    DateTime,
)
from sqlalchemy.orm import (
    relationship,
)
from imageupload.models import Base, User
from imageupload.models.storage.image import BaseImage
from sqlalchemy import func
from pyramid.compat import escape
from ..validator import (
    ValidationStatus,
    BaseValidator,
)


class Gallery(Base, BaseValidator):

    __tablename__ = 'galleries'
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False, index=True)
    description = Column(Text, nullable=True)
    created_on = Column(DateTime, server_default=func.now())
    updated_on = Column(DateTime, server_default=func.now(), server_onupdate=func.now())
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)

    user = relationship(
        "User",
        back_populates='galleries',
    )

    images = relationship(
        "GalleryImage",
        back_populates='gallery',
        uselist=True,
        primaryjoin='GalleryImage.gallery_id == Gallery.id',
        cascade='all, delete-orphan',
    )

    def __repr__(self):
        return escape(self.title)

    def validate(self,
                 title=None,
                 description=None):
        vstatus = ValidationStatus()
        if title is None:
            title = self.title
        if description is None:
            description = self.description
        if len(title) == 0 or len(description) == 0:
            vstatus.success = False
            vstatus.msg_stack = 'Title or description can not be empty!'
        return vstatus


class GalleryImage(Base, BaseImage):

    __tablename__ = 'gallery_images'
    id = Column(Integer, primary_key=True)
    gallery_id = Column(Integer, ForeignKey(Gallery.id), nullable=False)
    uploaded_on = Column(DateTime, server_default=func.now())

    gallery = relationship(
        "Gallery",
        back_populates='images',
    )
