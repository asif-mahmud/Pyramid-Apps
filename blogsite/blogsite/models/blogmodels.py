from .meta import Base
from sqlalchemy import (
    Integer,
    Text,
    Column,
    CheckConstraint,
    ARRAY,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import (
    relationship,
    backref,
)
from bcrypt import (
    hashpw,
    gensalt,
)
from pyramid.compat import escape
from datetime import datetime


class Blogger(Base):

    __tablename__ = 'bloggers'
    id = Column(Integer, primary_key=True)
    name = Column(Text, index=True, unique=True, nullable=False)
    __password = Column(Text, nullable=False)
    roles = Column(
        ARRAY(Text),
        default=['blogger', ],
    )

    blogs = relationship(
        'Blog',
        backref=backref('blogger'),
        uselist=True,
        cascade='all, delete-orphan',
        order_by='Blog.created_on',
        primaryjoin='Blogger.id == Blog.blogger_id',
    )

    posts = relationship(
        'Post',
        backref=backref('blogger'),
        uselist=True,
        order_by='Post.created_on',
    )

    __table_args__ = (
        CheckConstraint('char_length(name) > 0', name='name_len_check'),
    )

    def set_password(self, pw):
        if len(pw) > 0:
            self.__password = hashpw(
                pw.encode(encoding='utf-8'),
                gensalt()
            ).decode()

    def check_password(self, pw):
        if len(pw) > 0:
            return self.__password.encode(encoding='utf-8') == hashpw(
                pw.encode(encoding='utf-8'),
                self.__password.encode(encoding='utf-8')
            )

    def __repr__(self):
        return escape(self.name)


class Blog(Base):

    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True)
    title = Column(Text, index=True, unique=True, nullable=False)
    description = Column(Text, nullable=False)
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    blogger_id = Column(Integer, ForeignKey(Blogger.id), nullable=False)

    posts = relationship(
        'Post',
        backref=backref('blog'),
        uselist=True,
        cascade='all, delete-orphan',
        order_by='Post.created_on',
        primaryjoin='Blog.id == Post.blog_id',
    )

    def __repr__(self):
        return escape(self.title)

    def __html__(self):
        return escape(self.description)


class Post(Base):

    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False, unique=True, index=True)
    body = Column(Text, nullable=False)
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    blog_id = Column(Integer, ForeignKey(Blog.id), nullable=False)
    blogger_id = Column(Integer, ForeignKey(Blogger.id), nullable=False)

    def __repr__(self):
        return escape(self.title)

    def __html__(self):
        return escape(self.body)
