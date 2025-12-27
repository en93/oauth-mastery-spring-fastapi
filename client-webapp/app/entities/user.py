from __future__ import annotations
import uuid
from sqlalchemy import (
    DateTime,
    ServerOnUpdate,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
from app.database import Base


class User(Base, AsyncAttrs):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True
    )
    user_full_name: Mapped[str]
    primary_email: Mapped[str] = mapped_column(unique=True)
    primary_email_verified: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), server_onupdate=ServerOnUpdate(func.now())
    )

    auth_identities: Mapped[list["AuthIdentity"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )