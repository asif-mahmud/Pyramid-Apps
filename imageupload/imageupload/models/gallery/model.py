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
from datetime import datetime
from pyramid.compat import escape


class Gallery(Base):

    __tablename__ = 'galleries'
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False, index=True)
    description = Column(Text, nullable=True)
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)
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


class GalleryImage(Base, BaseImage):

    __tablename__ = 'gallery_images'
    id = Column(Integer, primary_key=True)
    gallery_id = Column(Integer, ForeignKey(Gallery.id), nullable=False)
    uploaded_on = Column(DateTime, default=datetime.now)

    gallery = relationship(
        "Gallery",
        back_populates='images',
    )
