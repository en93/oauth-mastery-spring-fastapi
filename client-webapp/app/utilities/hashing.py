from pwdlib import PasswordHash
from app.utilities.async_task import async_task

@async_task
def hash_password(password: str) -> str:
    """
    Hash the password and return it

    :param password: Plaintext of password
    :type password: str
    :return: Hashed password using recommended algorithm
    :rtype: str
    """
    password_hash = PasswordHash.recommended()
    return password_hash.hash(password)
