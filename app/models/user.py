#------------------------------
# User Model Class
# written by - BugsWriter
#------------------------------

import sqlalchemy as sa
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING
from app.db.base_class import Base


if TYPE_CHECKING:
    pass


class User(Base):
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    username = sa.Column(sa.String, index=True)
    email = sa.Column(sa.String, unique=True, index=True, nullable=False)
    hashed_password = sa.Column(sa.String, nullable=False)
    is_verified = sa.Column(sa.Boolean(), default=False)
    is_superuser = sa.Column(sa.Boolean(), default=False)
