# import uuid
# from sqlalchemy import select
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.entities import AuthIdentity


# class AuthIdentityRepository:
#     def __init__(self, session: AsyncSession):
#         self.session = session

#     async def create_auth_identity(
#         self,
#         user_id: uuid.UUID,
#         provider_type: str,
#         provider_id: str,
#         password_hash: str | None = None,
#         display_email: str | None = None,
#     ) -> AuthIdentity:
#         new_auth_identity = AuthIdentity(
#             user_id=user_id,
#             provider_type=provider_type,
#             provider_id=provider_id,
#             password_hash=password_hash,
#             display_email=display_email,
#         )
#         self.session.add(new_auth_identity)
#         await self.session.flush()
#         return new_auth_identity

#     async def get_by_provider(
#         self, provider_type: str, provider_id: str
#     ) -> AuthIdentity | None:
#         result = await self.session.execute(
#             select(AuthIdentity).where(
#                 AuthIdentity.provider_type == provider_type,
#                 AuthIdentity.provider_id == provider_id,
#             )
#         )
#         return result.scalars().first()
