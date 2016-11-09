from .meta import Base
from sqlalchemy import (
    Column,
    Text,
    Integer,
    ForeignKey,
)
from sqlalchemy.orm import (
    relationship,
)
from pyramid.compat import escape


class Pet(Base):

    type_id = Column(Integer, ForeignKey('pettype.id'), nullable=False)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    owner_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    type = relationship(
        'PetType',
        back_populates='pets',
    )

    owner = relationship(
        'User',
        back_populates='pets',
    )

    def __json__(self, request):
        return dict(
            type=escape(''.join(self.type.name)),
            name=escape(''.join(self.name)),
            owner=escape(''.join(self.owner.username)),
            description=escape(''.join(self.description)),
        )

    def __repr__(self):
        return escape(
            ''.join(self.name)
        )
