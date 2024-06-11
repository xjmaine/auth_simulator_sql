import sys
import os
from getpass import getpass
from repository.user_db import UserDatabase
from services.user_service import UserService

BASE_DIR = os.path.dirname(__file__)
STORAGE_PATH = os.path.join(BASE_DIR, "storage")
FILE_PATH = os.path.join(STORAGE_PATH, "data.csv")


class AuthSimulator:
    """AuthSimulator is a simple class that simulates an authentication system.
    It is a console application where the user can register, login, and logout.
    """

    __running = True

    def __init__(self):
        self.db = None
        self.service = UserService()
        self.__initialize_db()

    def __initialize_db(self):
        try:
            self.db = UserDatabase(file_to_connect_to=FILE_PATH)
        except (ValueError, TypeError, FileNotFoundError) as e:
            print(f"Error initializing database: {e}")
            self.__exiting()

    def __display_menu(self, menu: str) -> None:
        """Private method to display menu"""
        print(menu)

    def __get_user_choice(self) -> str:
        """Private method to get user choice"""
        try:
            return input("> ")
        except KeyboardInterrupt:
            self.__exiting()

    def __get_account_info(self) -> tuple[str, str, str]:
        """Private method to get account info"""
        email = input("Email: ")
        name = input("Full name: ")
        password = getpass(prompt="Password: ")
        return email, name, password

    def __get_login_info(self) -> tuple[str, str]:
        """Private method to get login info"""
        email = input("Email: ")
        password = getpass(prompt="Password: ")
        return email, password

    def __exiting(self) -> None:
        """Private method to exit application"""
        print("Exiting...\nThank you for your time spent with us.")
        self.__running = False
        sys.exit()

    def __user_menu(self, user):
        while True:
            self.__display_menu("""
===========================================
1. Get user info
2. Update user name
3. Logout
===========================================
""")
            choice = self.__get_user_choice()
            if choice == '1':
                print(user.get_user())
            elif choice == '2':
                print("You can only update your name.")
                name = input("New name: ")
                if name:
                    try:
                        user = self.service.update_user(
                            db=self.db, id=user.id, item={"name": name})
                        print("User updated successfully.")
                        print(user.get_user())
                    except Exception as e:
                        print(f"Failed to update user: {e}")
            elif choice == '3':
                try:
                    user = self.service.logout_user(db=self.db, user=user)
                    print(f"User {user.id} logged out.")
                    break
                except Exception as e:
                    print(f"Failed to logout: {e}")
                    break
            else:
                print("Invalid choice. Try again.")

    def run(self):
        """Run method to run the application."""
        while self.__running:
            self.__display_menu("""
Welcome to AuthSimulator!
Please select one of the following [1-3].
===========================================
1. Create an account.
2. Login to account.
3. Exit application.
===========================================
""")
            choice = self.__get_user_choice()
            if choice == '1':
                self.__display_menu("""
Please fill the form below.
*** All fields are required ***
*** Password will not display on screen ***
===========================================
""")
                email, name, password = self.__get_account_info()
                try:
                    user = self.service.create_user(
                        db=self.db, email=email, name=name, password=password)
                    print(
                        f"User created successfully. Your user ID is {user.id}")
                except Exception as e:
                    print(f"Failed to create user: {e}")
            elif choice == '2':
                self.__display_menu("""
Login Form
*** All fields are required ***
*** Password will not display on screen ***
===========================================
""")
                email, password = self.__get_login_info()
                try:
                    user = self.service.login_user(
                        db=self.db, email=email, password=password)
                    print("Logged in successfully!")
                    self.__user_menu(user)
                except Exception as e:
                    print(f"Login failed: {e}")
            elif choice == '3':
                self.__exiting()
            else:
                print("Invalid choice. Try again.")


if __name__ == '__main__':
    app = AuthSimulator()
    app.run()
