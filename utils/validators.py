import re


def email_validator(email: str) -> str:
    """Validate email address

    Args:
        email (str): Email address to validate

    Returns:
        bool: True if email is valid, False otherwise
    """
    if re.match(r"^[a-z][a-zA-Z0-9_.]+@[a-z]+\.[a-z]+", email):
        return email
    raise ValueError("Invalid email address!")


def password_validator(password: str) -> str:
    """Validate password

    Args:
        password (str): Password to validate

    Returns:
        bool: True if password is valid, False otherwise
    """
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long!")
    if not re.search(r'\d', password):
        raise ValueError("Password must contain at least one digit!")
    if not re.search(r'[A-Z]', password):
        raise ValueError("Password must contain at least one uppercase letter!")
    if not re.search(r'[a-z]', password):
        raise ValueError("Password must contain at least one lowercase letter!")
    return password
