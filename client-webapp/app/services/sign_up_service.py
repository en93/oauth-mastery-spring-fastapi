from app.models import SignUpForm
from pwdlib import PasswordHash


async def sign_up(sign_up_form: SignUpForm):

    # Salt password, hash it
    # Move to utility function later
    password_hash = PasswordHash.recommended()
    hashed_password = password_hash.hash(sign_up_form.password)
    return hashed_password
