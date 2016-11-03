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

    type = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    owner_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    owner = relationship(
        'User',
        back_populates='pets',
    )

    def __repr__(self):
        return escape(
            self.name
        )
