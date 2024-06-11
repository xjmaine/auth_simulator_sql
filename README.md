# AuthSimulator

AuthSimulator is a console application that simulates user authentication and user management functionalities. It is built using Python and incorporates the principles of object-oriented programming (OOP), including interfaces, abstract classes, and the four pillars of OOP.

AuthSimulator is licensed under the [MIT License](LICENSE).
## Functionality

AuthSimulator provides the following functionalities:

1. Creating a User: The application allows you to create a new user by providing the necessary information such as username, password, and email.

2. Logging in a User: Once a user is created, you can log in using the username and password. The application validates the credentials and grants access if they are correct.

3. Logging out a User: After logging in, you have the option to log out from the current session. This will terminate the user's access and require re-authentication for further actions.

4. Updating a Logged-in User: After logging in, you have the option to update your user information, including the username, password, and email.

## Installation

To run AuthSimulator, you need to have Python installed on your system. If you don't have Python installed, you can download it from the official Python website (https://www.python.org/downloads/).

Once you have Python installed, you can clone the AuthSimulator project repository to your local machine using the following command:

```
git clone https://github.com/waltob123/auth_simulator.git
```

## Usage

After cloning the project, navigate to the project directory in your terminal or command prompt. To run the application, use the following command:

```
python app.py [csv_file]
```

The `csv_file` argument is optional. If you provide a CSV file as an argument, the application will use it to store user data. If no CSV file is provided, the application will use a default storage file.

## Contributing

If you would like to contribute to AuthSimulator, feel free to fork the repository and submit a pull request. Your contributions are greatly appreciated!

## License

AuthSimulator is licensed under the [MIT License](LICENSE).
