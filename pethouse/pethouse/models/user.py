from .meta import Base
from sqlalchemy import (
    Column,
    Text,
)
from sqlalchemy.orm import (
    relationship,
)
from bcrypt import (
    hashpw,
    gensalt
)
from pyramid.compat import escape


class User(Base):

    username = Column(Text, index=True, nullable=False)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    password_hash = Column(Text, nullable=False)

    pets = relationship(
        'Pet',
        back_populates='owner',
        uselist=True,
        cascade='all, delete-orphan',
        primaryjoin='Pet.owner_id == User.id',
    )

    def set_password(self, pw):
        self.password_hash = hashpw(
            pw.encode(encoding='utf-8'),
            gensalt()
        ).decode()

    def check_password(self, pw):
        return self.password_hash.encode(encoding='utf-8') == hashpw(
            pw.encode(encoding='utf-8'),
            self.password_hash.encode(encoding='utf-8')
        )

    def __repr__(self):
        return escape(
            '{} {}'.format(
                self.first_name,
                self.last_name
            )
        )
