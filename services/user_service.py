from repository.user_db import UserDatabase
from models.user import User

class UserService:
    """User servic class"""

    def create_user(self, db: UserDatabase, email: str, name: str, password: str) -> User:
        """Method to create a new user

        Args:
            db (UserDatabase): database instance
            email (str): email of the user
            name (str): name of the user
            password (str): password of the user

        Returns:
            User: user object created
        """
        if email is None:
            raise ValueError("email cannot be None")

        if password is None:
            raise ValueError("password cannot be None")

        if name is None:
            raise ValueError("name cannot be None")

        new_user = User(email=email, name=name)
        new_user.password = password
        saved_user = db.add(item=new_user)
        db.save()
        return saved_user

    def update_user(self, db: UserDatabase, id: str, item: dict) -> User:
        """Method to update a user object

        Args:
            db (UserDatabase): database instance
            id (str): id of user to update
            item (dict): things to update user object with

        Returns:
            User: updated user object
        """
        updated_user = db.update(id=id, item=item)
        db.save()
        return updated_user

    def delete_user(self, db: UserDatabase, id: str) -> None:
        """Method to delete a user from database

        Args:
            db (UserDatabase): database instance
            id (str): id of user to delete
        """
        db.delete(id=id)
        db.save()

    def get_all_users(self, db: UserDatabase) -> list[User]:
        """Method to get all users

        Args:
            db (UserDatabase): database instance

        Returns:
            list[User]: list of all users
        """
        return list(db.all())

    def get_one_user(self, db: UserDatabase, id: str) -> User | None:
        """Method to get a user

        Args:
            db (UserDatabase): database instance
            id (str): id of user to get

        Returns:
            User | None: user object or none
        """
        return db.get(id=id)
