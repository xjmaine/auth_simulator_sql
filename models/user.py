from utils.validators import email_validator, password_validator
from .base import Base

class User(Base):
    """User model class"""

    def __init__(self, email: str, name: str, id: str = None):
        """Constructor for the User class

        Args:
            email (str): Email of the user
            password (str): Password of the user
            name (str): Full name of the user
        """
        super().__init__(id)

        try:
            self.__email = email_validator(email)
        except ValueError as e:
            raise ValueError(e)

        self.__name = name
        self.__password = None

    @property
    def email(self) -> str:
        """Getter for the email attribute"""
        return self.__email

    @property
    def name(self) -> str:
        """Getter for the name attribute"""
        return self.__name

    @property
    def password(self) -> None:
        """Getter for the password attribute"""
        raise AttributeError("Password is not accessible")

    @password.setter
    def password(self, password: str) -> None:
        """Setter for the password attribute

        Args:
            password (str): The password to set
        """
        try:
            self.__password = password_validator(password)
        except ValueError as e:
            raise ValueError(e)

    def __repr__(self) -> str:
        """String representation of the User object"""
        return f"{self.__class__.__name__}('email={self.__email}', 'password={self.__password}', 'name={self.__name}', 'id={self.__id}')"

    def __str__(self) -> str:
        """String representation of the User object"""
        return f"User: {self.__name} <{self.__email}>"

    def __eq__(self, other) -> bool:
        """Equality method for the User class

        Args:
            other (User): The other User object to compare

        Returns:
            bool: True if the objects are equal, False otherwise
        """
        if not isinstance(other, User):
            return False
        return self.__id == other.id
