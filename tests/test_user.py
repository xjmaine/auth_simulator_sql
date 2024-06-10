import unittest
from unittest import TestCase
from models.user import User


class TestUser(TestCase):
    """TestUser is a class that tests the User model class

    Args:
        TestCase: Base class for all tests
    """

    def test_user_creation_with_invalid_email(self):
        """Test user creation"""
        with self.assertRaises(ValueError):
            User(email="Abc@google.com",
                 name="John Doe")

    def test_user_creation_with_invalid_password(self):
        """Test user creation"""
        user = User(email="abc@google.com", name="John Doe")
        with self.assertRaises(ValueError):
            user.password = "password1"

    def test_get_user_password(self):
        """Test user creation"""
        user = User(email="abc@google.com", name="John Doe")
        with self.assertRaises(AttributeError):
            user.password

    def test_user_creation_with_invalid_id(self):
        """Test user creation"""
        with self.assertRaises(ValueError):
            User(email="abc@google.com", name="John Doe", id="123")

    def test_user_creation_with_valid_id(self):
        """Test user creation"""
        user = User(email="abc@google.com", name="John Doe",
                    id="123e4567-e89b-12d3-a456-426614174000")
        self.assertEqual(user.id, "123e4567-e89b-12d3-a456-426614174000")

    def test_user_creation_with_valid_password(self):
        """Test user creation"""
        user = User(email="abc@google.com", name="John Doe")
        user.password = "Password1"

    def test_user_to_dict(self):
        """Test user to_dict method"""
        user = User(email="abc@google.com", name="John Doe")
        user.password = "Password1234"
        self.assertIsInstance(user.to_dict(), dict)
        self.assertEqual(user.email, user.to_dict().get('email'))

    def test_user_with_created_at(self):
        """Test user creation with created_at"""
        user = User(email="abc@google.com", name="John Doe",
                    created_at="09 June 2024 : 12:53:44")
        self.assertEqual(user.to_dict().get('created_at'),
                         "09 June 2024 : 12:53:44")

    def test_user_with_invalid_created_at(self):
        """Test user creation with invalid created_at"""
        with self.assertRaises(ValueError):
            User(email="abc@google.com", name="John Doe", created_at="09/06/2020")

    def test_inequality_of_two_users(self):
        """Test if two user objects are equal"""
        user1 = User(email="abc@google.com", name="John Doe")
        user2 = User(email="liam@google.com", name="Liam Black")
        self.assertNotEqual(user1, user2)

    def test_equality_of_two_users(self):
        """Test if two user objects are equal"""
        user1 = User(email="abc@google.com", name="John Doe")
        self.assertEqual(user1, user1)

    def test_get_item(self):
        """Test the get_item method of the User class"""
        user = User(email="abc@google.com", name="John Doe")
        self.assertTrue("password" not in user.get_user().keys())


if __name__ == '__main__':
    unittest.main()
