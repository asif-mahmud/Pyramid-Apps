from ..models import Base
from sqlalchemy import (
    Column,
    Text,
)
from sqlalchemy.orm import (
    relationship,
)
from pyramid.compat import escape


class PetType(Base):

    name = Column(Text, nullable=False, unique=True)

    pets = relationship(
        'Pet',
        back_populates='type',
        uselist=True,
        primaryjoin='Pet.type_id == PetType.id',
        cascade='all, delete-orphan',
    )

    def __json__(self, request):
        return dict(
            id=self.id,
            name=escape(''.join(self.name)),
        )

    def __repr__(self):
        return escape(''.join(self.name))
