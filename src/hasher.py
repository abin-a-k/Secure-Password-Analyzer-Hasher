from argon2 import PasswordHasher
from argon2.exceptions import (
    VerifyMismatchError,
    VerificationError,
    InvalidHashError
)


password_hasher = PasswordHasher()


def hash_password(password):
    """
    Hash a password using Argon2id.
    """

    hashed_password = password_hasher.hash(password)

    return hashed_password


def verify_password(password, hashed_password):
    """
    Verify a password against its stored hash.
    """

    try:
        password_hasher.verify(hashed_password, password)
        return True

    except VerifyMismatchError:
        return False

    except InvalidHashError:
        return False

    except VerificationError:
        return False