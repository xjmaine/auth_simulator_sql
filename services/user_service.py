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

    def login_user(self, db: UserDatabase, email: str, password: str) -> User:
        """Method to log a user in

        Args:
            db (UserDatabase): database instance
            email (str): email of the user
            password (str): password of the user

        Returns:
            User: the user object
        """
        if email is None:
            raise ValueError("email cannot be None")

        if password is None:
            raise ValueError("password cannot be None")

        user = db.get_user_by_email(email=email)

        if not user:
            raise ValueError(f"user with {email} does not exist")

        if user.check_password_is_same(password=password):
            logged_in_user = db.update(id=user.id, item={"is_logged_in": True})
            db.save()
            return logged_in_user
        raise ValueError("password is incorrect.")

    def logout_user(self, db: UserDatabase, user: User) -> User:
        """Method to logout user

        Args:
            db (UserDatabase): database instance
            user (User): user to be logged out
        """
        if not isinstance(user, User):
            raise TypeError(f"user {user} must be of type User")

        if user is None:
            raise ValueError("user cannot be None")

        if not user.is_logged_in:
            raise Exception(f"user {user.id} has already been logged out")

        logged_out_user = db.update(id=user.id, item={"is_logged_in": False})
        db.save()
        return logged_out_user
