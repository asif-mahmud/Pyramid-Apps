from imageupload.models import (
    Base,
    BaseValidator,
    ValidationStatus,
)
from imageupload.models.storage.image import BaseImage
from sqlalchemy import (
    Column,
    Integer,
    Text,
    ARRAY,
    ForeignKey,
    DateTime,
)
from sqlalchemy.orm import (
    relationship,
)
from bcrypt import (
    hashpw,
    gensalt,
)
from sqlalchemy import func


class User(Base, BaseValidator):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True, nullable=False, index=True)
    _password_hash = Column(Text, nullable=False)
    roles = Column(ARRAY(Text), default=['user', ], nullable=False)
    joined_on = Column(DateTime, server_default=func.now(), nullable=False)

    profile_picture = relationship(
        "ProfilePicture",
        back_populates='user',
        cascade='all, delete-orphan',
        uselist=False,
    )

    galleries = relationship(
        "Gallery",
        back_populates='user',
        uselist=True,
        cascade='all, delete-orphan',
    )

    def validate(self,
                 dbsession,
                 name=None,
                 password=None,
                 password_check=None,
                 check_password=False,):
        v = ValidationStatus()
        v.clear()
        if name is None:
            name = self.name

        if len(name) < 4:
            v.success = False,
            v.msg_stack = 'Name must be at least 4 characters long.'
        else:
            for ch in name:
                if not ch.isalnum():
                    v.success = False
                    v.msg_stack = 'Name can contains letters and numbers only.'
                    break
            if dbsession is not None and\
               dbsession.query(User).filter_by(
                name=name
               ).first() is not None:
                v.success = False
                v.msg_stack = 'Username is already taken!'

        if password is not None:
            if len(password) < 6:
                v.success = False
                v.msg_stack = 'Password must be at least 6 characters long.'
            if password_check is not None and \
               password != password_check:
                v.success = False
                v.msg_stack = 'Password did not match!'
        if check_password and not self.check_password(password):
            v.success = False
            v.msg_stack = 'Wrong password!'
        return v

    def set_password(self, pw):
        self._password_hash = hashpw(
            pw.encode(encoding='utf-8'),
            gensalt()
        ).decode()

    def check_password(self, pw):
        return self._password_hash.encode(
            encoding='utf-8'
        ) == hashpw(
            pw.encode(encoding='utf-8'),
            self._password_hash.encode(encoding='utf-8')
        )


class ProfilePicture(BaseImage, Base):

    __tablename__ = 'profile_pictures'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey(User.id), nullable=False)

    user = relationship(
        "User",
        back_populates='profile_picture',
    )
