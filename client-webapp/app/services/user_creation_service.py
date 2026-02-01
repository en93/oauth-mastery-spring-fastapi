from app.models.user_creation import user_creation

from sqlalchemy.ext.asyncio import AsyncSession
# from app.repositories.user_repository import UserRepository
# from app.repositories.auth_identity_repository import AuthIdentityRepository
from app.utilities.hashing import hash_password


async def create_user(sign_up_form: user_creation, session: AsyncSession):
    # user_repo = UserRepository(session)
    # auth_identity_repo = AuthIdentityRepository(session)

    hashed_pw = await hash_password(sign_up_form.password)
    print(hashed_pw)

    # async with session.begin():
    #     new_user = await user_repo.create_user(
    #         user_full_name=sign_up_form.username,
    #         primary_email=sign_up_form.email
    #     )
    #     await auth_identity_repo.create_auth_identity(
    #         user_id=new_user.id,
    #         provider_type="password",
    #         provider_id=sign_up_form.email,
    #         password_hash=hashed_password,
    #         display_email=sign_up_form.email
    #     )

    return "sign up complete"
