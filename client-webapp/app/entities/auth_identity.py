from __future__ import annotations
import uuid
from sqlalchemy import (

    DateTime,
    ServerOnUpdate,
    func,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
from app.database import Base


class AuthIdentity(Base, AsyncAttrs):
    __tablename__ = "auth_identities"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True
    )
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    provider_type: Mapped[str]
    provider_id: Mapped[str]
    password_hash: Mapped[str | None]
    display_email: Mapped[str | None]
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), server_onupdate=ServerOnUpdate(func.now())
    )

    user: Mapped["User"] = relationship(back_populates="auth_identities")

    __table_args__ = (
        UniqueConstraint("provider_type", "provider_id"),
        UniqueConstraint("user_id", "provider_type"),
    )
