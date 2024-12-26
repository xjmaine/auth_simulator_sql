import bcrypt

def password_hash(password):
    """_summary_

    Args:
        password (_type_): _description_
    """
    char_gen = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), char_gen).decode('utf-8')


def  verify_password(password, hashed_password):
    """_summary_

    Args:
        password (_type_): _description_
        hashed_password (bool): _description_
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))