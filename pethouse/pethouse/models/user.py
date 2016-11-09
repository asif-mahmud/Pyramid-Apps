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
from .validation import ValidationStatus


class User(Base):

    username = Column(Text, index=True, nullable=False, unique=True)
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

    def validate(self,
                 username=None,
                 first_name=None,
                 last_name=None,
                 password=None,
                 password_retype=None):
        if username is None:
            username = self.username
        if first_name is None:
            first_name = self.first_name
        if last_name is None:
            last_name = self.last_name

        vstatus = ValidationStatus(status=True)
        if len(username) == 0:
            vstatus.error('Username can not be empty.')
        if len(first_name) == 0:
            vstatus.error('First name can not be empty.')
        if len(last_name) == 0:
            vstatus.error('Last name can not be empty.')

        if password is not None:
            if password != password_retype:
                vstatus.error('Password mismatched.')
            if len(password) < 4:
                vstatus.error('Password must be at least 4 characters long.')
        return vstatus

    def __json__(self, request):
        return dict(
            username=escape(''.join(self.username)),
            first_name=escape(''.join(self.first_name)),
            last_name=escape(''.join(self.last_name)),
            pets=self.pets,
        )

    def __repr__(self):
        return escape(
            '{} {}'.format(
                ''.join(self.first_name),
                ''.join(self.last_name)
            )
        )
