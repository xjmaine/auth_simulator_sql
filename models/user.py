from services import hash_gen
from utils.validators import email_validator, password_validator
from .base import Base

class User(Base):
    """User model class"""

    def __init__(self, email: str, name: str,
                 id: str = None, created_at: str = None, updated_at: str = None):
        """Constructor for the User class

        Args:
            email (str): Email of the user
            password (str): Password of the user
            name (str): Full name of the user
        """
        super().__init__(id, created_at, updated_at)

        try:
            self.__email = email_validator(email)
        except ValueError as e:
            raise ValueError(e)

        self.__name = name
        self.__password = None
        self.__is_logged_in = False

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

    @property
    def is_logged_in(self) -> bool:
        """Getter for is_logged_in attribute"""
        return self.__is_logged_in

    @name.setter
    def name(self, name: str) -> None:
        """Setter for the name attribute

        Args:
            name (str): The name to set
        """
        self.__name = name

    @email.setter
    def email(self, email: str) -> None:
        """Setter for the email attribute

        Args:
            email (str): The email to set
        """
        try:
            self.__email = email_validator(email)
        except ValueError as e:
            raise ValueError(e)

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

    @is_logged_in.setter
    def is_logged_in(self, value: bool) -> None:
        """Setter for is_logged_in attribute

        Args:
            value (bool): The value to set
        """
        self.__is_logged_in = value

    def check_password_is_same(self, password: str) -> bool:
        """Check if the password provided is the same

        Args:
            password (str): password to check

        Returns:
            bool: True or False
        """
        # return self.__password == password
        return hash_gen.verify_password(password, self.__password)
    

    def to_dict(self) -> dict:
        """Method to convert object to a python dictionary

        Returns:
            dict: Dictionary representation of object
        """
        return {
            "id": self.id,
            "email": self.email,
            "password": self.__password,
            "name": self.name,
            "is_logged_in": self.is_logged_in,
            "created_at": self.created_at.strftime("%d %B %Y : %H:%M:%S"),
            "updated_at": None if self.updated_at == None else self.updated_at.strftime("%d %B %Y : %H:%M:%S")
        }

    def get_user(self) -> dict:
        """Method to return the user object

        Returns:
            dict: Dictionary representation of object
        """
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "is_logged_in": self.is_logged_in,
            "created_at": self.created_at.strftime("%d %B %Y : %H:%M:%S"),
            "updated_at": None if self.updated_at == None else self.updated_at.strftime("%d %B %Y : %H:%M:%S")
        }

    def __repr__(self) -> str:
        """String representation of the User object"""
        return f"{self.__class__.__name__}('email={self.email}', 'name={self.name}', 'id={self.id}')"

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
        return self.id == other.id
