from app.models.base import Base


class user_creation(Base):
    email: str
    name: str
    password: (
        str  #  todo update to mask when output, add validation of length and complexity
    )
