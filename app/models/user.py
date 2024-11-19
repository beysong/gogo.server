

from app.extensions import db, ma
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, DateTime, Integer, String, Date, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from .base import Base


class User(Base):
    __tablename__ = "user"
    
    name: Mapped[str] = mapped_column(String(20))
    username: Mapped[str] = mapped_column(String(20))
    mobile: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(36))
    avatar: Mapped[str] = mapped_column(String(128))
    password_hash: Mapped[str] = mapped_column(String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"<User id={self.id}, name={self.name}, created_at={self.created_at}, updated_at={self.updated_at}, is_delete={self.is_delete}>"

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User