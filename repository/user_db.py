import csv
import os
import io
from datetime import datetime, timezone
from typing import Generator
from interfaces.db import Database
from models.user import User


class UserDatabase(Database):
    """UserDatabase class.

    Args:
        Database: Database interface
    """
    
    __FIELDNAMES = ['id', 'email', 'name', 'password', 'created_at', 'updated_at']
    __UPDATABLE_FIELDS = ['email', 'name', 'password']
    __users = []
    
    def __init__(self, file_to_connect_to: str) -> None:
        """Constructor for UserDatabase class

        Args:
            file_to_connect_to (string): File where data is going to be stored

        Returns:
            None
        """
        if file_to_connect_to is None:
            raise ValueError('File cannot be None')

        if not file_to_connect_to.endswith('.csv'):
            raise TypeError('File type must be a json. Eg abc.json')

        self._file = file_to_connect_to

        if os.path.getsize(self._file) > 0:
            self.__load()

    @property
    def users(self) -> list:
        """Property to get the users

        Returns:
            list: List of users
        """
        return UserDatabase.__users

    def __open_file(self, mode: str = None) -> io.TextIOWrapper:
        """Private method to open the database file with a mode

        Args:
            mode (str, optional): Mode to open file in. Defaults to None.

        Raises:
            FileNotFoundError: If the file does not exist

        Returns:
            io.TextIOWrapper: The file object
        """
        if mode is None:
            mode = 'r'

        try:
            file = open(self._file, mode=mode, newline='')
        except FileNotFoundError as e:
            raise FileNotFoundError(f'File {self._file} was not found.')
        
        return file

    def __close_file(self, file: io.TextIOWrapper) -> None:
        """Private method to close the database file
        """
        if file is None:
            raise ValueError(f"File {file} cannot be NoneType")

        if not file.closed:
            file.close()

    def __load(self) -> None:
        """Private method to load users into a list

        Raises:
            FileNotFoundError: If the file does not exist

        Returns:
            None
        """
        file = self.__open_file(mode="r")
        reader = csv.DictReader(f=file)
        UserDatabase.__users = [row for row in reader]
        self.__close_file(file)

    def check_email_exists(self, email: str) -> bool:
        """Method to check if email already exists

        Args:
            email (str): email to check

        Returns:
            bool: true or false
        """
        for user in UserDatabase.__users:
            if user.get('email') == email:
                return True
        return False

    def add(self, item: User) -> User:
        """Adds a user object to the database

        Args:
            item (User): User object to add to the database

        Raises:
            ValueError: If the user already exists

        Returns:
            User: the user object added to the database
        """
        if item is None:
            raise ValueError("Item cannot be None")

        if not isinstance(item, User):
            raise TypeError("item must be of type User")

        if self.get(item.id) is not None:
            raise ValueError(f"user with id {item.id} already exists")

        if self.check_email_exists(item.email):
            raise ValueError(f"email {item.email} already exists")

        UserDatabase.__users.append(item.to_dict())
        return item

    def update(self, id: str, item: dict) -> User:
        """Updates a user object in the database

        Args:
            id (str): unique identity of user to update
            item (dict): item to update the user with

        Returns:
            User: the updated user object
        """
        if item is None:
            raise ValueError("item cannot be None")

        if not isinstance(item, dict):
            raise TypeError("item must be of type dict")

        if self.get(id) is None:
            return None

        user_obj, user_dict = self.get(id)
        for key, value in item.items():
            if key in UserDatabase.__UPDATABLE_FIELDS and value is not None:
                setattr(user_obj, key, value)
                user_dict.update({key: value})
        setattr(user_obj, 'updated_at', datetime.now(tz=timezone.utc))
        user_dict.update({'updated_at': user_obj.to_dict().get('updated_at')})
        return user_obj
        

    def all(self) -> Generator[User, None, None]:
        """Method to get all users from the database

        Returns:
            Generator[User, None, None]: A generator of all users in the database
        """
        if len(UserDatabase.__users) != 0:
            for user in UserDatabase.__users:
                result = User(
                    email=user.get('email'),
                    name=user.get('name'),
                    id=user.get('id'),
                    created_at=user.get('created_at'),
                    updated_at=user.get('updated_at')
                )
                result.password = user.get('password')
                yield result
        else:
            return []

    def delete(self, id: str):
        """Method to delete a user from the database

        Args:
            id (str): The id of the user to delete
        """
        if self.get(id) is None:
            raise ValueError(f"User with id {id} does not exist")

        _, user_dict = self.get(id)

        UserDatabase.__users.remove(user_dict)
        return

    def get(self, id: str) -> tuple[User, dict]:
        """Method to get a user object from the database

        Args:
            id (str): The id of the user to get

        Returns:
            User: The user object
        """
        for user in UserDatabase.__users:
            if user.get('id') == id:
                result = User(
                    email=user.get('email'),
                    name=user.get('name'),
                    id=user.get('id'),
                    created_at=user.get('created_at'),
                    updated_at=user.get('updated_at')
                )
                result.password = user.get('password')
                return result, user
        return None

    def save(self) -> None:
        """Method to save the database to the file
        """
        file = self.__open_file(mode='w')
        writer = csv.DictWriter(f=file, fieldnames=UserDatabase.__FIELDNAMES)
        writer.writeheader()
        writer.writerows(UserDatabase.__users)
        self.__close_file(file)
        return
