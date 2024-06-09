import unittest
from unittest import TestCase
from utils.validators import email_validator, password_validator


class TestValidators(TestCase):
    """Test the validators module.

    Args:
        TestCase: Base class for test cases
    """

    def test_email_validator(self):
        """Test the email_validator function."""
        self.assertEqual(email_validator("kwasiasamoah18@outlook.com"), "kwasiasamoah18@outlook.com")

    def test_password_validator(self):
        """Test the password_validator function."""
        self.assertEqual(password_validator("Password1234"), "Password1234")

    def test_invalid_email_validator_without_domain(self):
        """Test the email_validator function with an invalid email."""
        with self.assertRaises(ValueError):
            email_validator("kwasiasamoah18@outlook")

    def test_invalid_email_validator_without_username(self):
        """Test the email_validator function with an invalid email."""
        with self.assertRaises(ValueError):
            email_validator("@outlook.com")

    def test_invalid_email_validator_beginning_with_special_character(self):
        """Test the email_validator function with an invalid email."""
        with self.assertRaises(ValueError):
            email_validator(".kwasiasamoah18@outlook.com")

    def test_invalid_email_validator_beginning_with_number(self):
        """Test the email_validator function with an invalid email."""
        with self.assertRaises(ValueError):
            email_validator("1asamoah@outlook.com")

    def test_invalid_email_validator_without_at_symbol(self):
        """Test the email_validator function with an invalid email."""
        with self.assertRaises(ValueError):
            email_validator("kwasiasamoah18outlook.com")

    def test_invalid_email_validator_without_dot(self):
        """Test the email_validator function with an invalid email."""
        with self.assertRaises(ValueError):
            email_validator("kwasiasamoah18@outlookcom")

    def test_invalid_email_validator_beginning_with_capital_letter(self):
        """Test the email_validator function with an invalid email."""
        with self.assertRaises(ValueError):
            email_validator("Kwasiasamoah@outlook.com")

    def test_invalid_email_validator_with_domain_as_number(self):
        """Test the email_validator function with an invalid email."""
        with self.assertRaises(ValueError):
            email_validator("kwasiasamoah18@outlook.12")

    def test_invalid_email_email_validator_with_empty_string(self):
        """Test the email_validator function with an invalid email."""
        with self.assertRaises(ValueError):
            email_validator("")

    def test_invalid_email_validator_with_special_characters(self):
        """Test the email_validator function with an invalid email."""
        with self.assertRaises(ValueError):
            email_validator("kwasiasamoah18@outlook!com")

    def test_invalid_email_validator_with_space(self):
        """Test the email_validator function with an invalid email."""
        with self.assertRaises(ValueError):
            email_validator("kwasiasamoah18 @outlook.com")

    def test_invalid_email_validator_with_no_email(self):
        """Test the email_validator function with an invalid email."""
        with self.assertRaises(ValueError):
            email_validator("kwasiasamoah18")

    def test_invalid_password_validator_with_less_than_eight_characters(self):
        """Test the password_validator function with an invalid password."""
        with self.assertRaises(ValueError):
            password_validator("Pass123")

    def test_invalid_password_validator_without_digit(self):
        """Test the password_validator function with an invalid password."""
        with self.assertRaises(ValueError):
            password_validator("Password")

    def test_invalid_password_validator_without_uppercase_letter(self):
        """Test the password_validator function with an invalid password."""
        with self.assertRaises(ValueError):
            password_validator("password123")

    def test_invalid_password_validator_without_lowercase_letter(self):
        """Test the password_validator function with an invalid password."""
        with self.assertRaises(ValueError):
            password_validator("PASSWORD123")

    def test_invalid_password_validator_with_empty_string(self):
        """Test the password_validator function with an invalid password."""
        with self.assertRaises(ValueError):
            password_validator("")

    def test_invalid_password_validator_with_spaces(self):
        """Test the password_validator function with an invalid password."""
        with self.assertRaises(ValueError):
            password_validator("        ")


if __name__ == '__main__':
    unittest.main()
