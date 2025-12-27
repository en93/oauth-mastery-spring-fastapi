# from __future__ import annotations
# import uuid
# from typing import Annotated

# from fastapi import FastAPI, Form
# from pydantic import BaseModel
# from sqlalchemy import (
#     Column,
#     String,
#     Boolean,
#     DateTime,
#     func,
#     ForeignKey,
#     UniqueConstraint,
# )
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column
# from sqlalchemy.ext.asyncio import AsyncAttrs


# from app.database import Base


# class SignUpForm(BaseModel):
#     username: str
#     email: str
#     password: str
#     greeting: str


# class User(Base, AsyncAttrs):
#     __tablename__ = "users"

#     id: Mapped[uuid.UUID] = mapped_column(
#         UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
#     )
#     user_full_name: Mapped[str]
#     primary_email: Mapped[str] = mapped_column(unique=True)
#     primary_email_verified: Mapped[bool] = mapped_column(default=False)
#     created_at: Mapped[DateTime] = mapped_column(
#         DateTime(timezone=True), server_default=func.now()
#     )
#     updated_at: Mapped[DateTime] = mapped_column(
#         DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
#     )

#     auth_identities: Mapped[list["AuthIdentity"]] = relationship(
#         back_populates="user", cascade="all, delete-orphan"
#     )




