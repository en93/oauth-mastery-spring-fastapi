from app.models.signup_form import SignUpForm
from pwdlib import PasswordHash
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository
from app.repositories.auth_identity_repository import AuthIdentityRepository


async def sign_up(sign_up_form: SignUpForm, session: AsyncSession):
    user_repo = UserRepository(session)
    auth_identity_repo = AuthIdentityRepository(session)

    # Salt password, hash it
    # Move to utility function later
    password_hash = PasswordHash.recommended()
    hashed_password = password_hash.hash(sign_up_form.password)
    
    async with session.begin(): 
        new_user = await user_repo.create_user(
            user_full_name=sign_up_form.username,
            primary_email=sign_up_form.email
        )
        await auth_identity_repo.create_auth_identity(
            user_id=new_user.id,
            provider_type="password",
            provider_id=sign_up_form.email,
            password_hash=hashed_password,
            display_email=sign_up_form.email
        )

    return "sign up complete"
