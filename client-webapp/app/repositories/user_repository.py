# import uuid
# from sqlalchemy import select
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.entities import User


# class UserRepository:
#     def __init__(self, session: AsyncSession):
#         self.session = session

#     async def create_user(self, user_full_name: str, primary_email: str) -> User:
#         new_user = User(user_full_name=user_full_name, primary_email=primary_email)
#         self.session.add(new_user)
#         await self.session.flush()
#         return new_user

#     async def get_user_by_id(self, user_id: uuid.UUID) -> User | None:
#         result = await self.session.execute(select(User).where(User.id == user_id))
#         return result.scalars().first()

#     async def get_user_by_email(self, email: str) -> User | None:
#         result = await self.session.execute(
#             select(User).where(User.primary_email == email)
#         )
#         return result.scalars().first()
