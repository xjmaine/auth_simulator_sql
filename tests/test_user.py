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
        user = User(email="abc@google.com", name="John Doe", id="123e4567-e89b-12d3-a456-426614174000")
        self.assertEqual(user.id, "123e4567-e89b-12d3-a456-426614174000")

    def test_user_creation_with_valid_password(self):
        """Test user creation"""
        user = User(email="abc@google.com", name="John Doe")
        user.password = "Password1"


if __name__ == '__main__':
    unittest.main()
