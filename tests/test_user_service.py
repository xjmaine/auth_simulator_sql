import unittest
from unittest import TestCase
from services.user_service import UserService
from repository.user_db import UserDatabase
from models.user import User


class TestUserService(TestCase):
    """Test user service

    Args:
        TestCase: base class for all tests
    """

    def setUp(self) -> None:
        self.file = "/home/walter_obrien/Documents/tutorials/python/oop_project/tests/data/test_user_service_db.csv"
        self.db = UserDatabase(file_to_connect_to=self.file)
        self.service = UserService()

    # uncomment this out
    # def test_create_user_service(self):
    #     """Test create_user method of user service
    #     Please make sure to change the email befor you ran this test.
    #     """
    #     self.assertIsInstance(self.service.create_user(
    #         db=self.db, email="eben@google.com", name="Ebenezer Smith", password="Man12344man"
    #     ), User)

    def test_create_user_service_with_invalid_email_and_password(self):
        """Test create_user method of user service with invalid email and password"""
        with self.assertRaises(ValueError):
            self.service.create_user(email="", name="Ebenzer Smith", 
                                password="Password1244", db=self.db)
            self.service.create_user(email="eben@google.com", name="Ebenezer Smith",
                                password="eben1234", db=self.db)

    def test_create_user_service_with_existing_email(self):
        """Test create_user method of user service with existing email"""
        with self.assertRaises(ValueError):
            self.service.create_user(
                db=self.db, email="abc@google.com", name="John Doe", password="Man12344man"
            )

    def test_update_user_service(self):
        """Test update_user method of user service
        """
        updated_user = self.service.update_user(id="a9e80d13-f3c5-4b93-989b-1c5c39bdef3e",
                                                db=self.db, item={
                                                    "name": "Ebenezer Doe"})
        self.assertEqual(updated_user.name, "Ebenezer Doe")
        self.assertIsNone(self.service.update_user(db=self.db, id=None, item={}))
        with self.assertRaises(ValueError):
            self.service.update_user(db=self.db, id="a9e80d13-f3c5-4b93-989b-1c5c39bdef3e", item=None)

        with self.assertRaises(TypeError):
            self.service.update_user(db=self.db, id="a9e80d13-f3c5-4b93-989b-1c5c39bdef3e", item="hello")

    # uncomment this out
    # def test_delete_user_service(self):
    #     """Test delete_user method of user service
    #     """
    #     with self.assertRaises(ValueError):
    #         self.service.delete_user(
    #             db=self.db, id="62221787-09c5-4136-861a-7ea06d953283"
    #         )

    #     """
    #     Always make sure to copy any id from row 2 or beyond from test_user_service_db.csv 
    #     """
    #     self.assertIsNone(self.service.delete_user(
    #         db=self.db, id="5d0df9d7-97a6-4277-b8f8-78e93fb9e9eb"
    #     ))

    def test_get_all_users_service(self):
        """Test get_all_users service
        """
        self.assertIsInstance(self.service.get_all_users(db=self.db), list)

    def test_get_one_user_service(self):
        """Test get_one_user service"""
        self.assertEqual(self.service.get_one_user(
            db=self.db, id="a9e80d13-f3c5-4b93-989b-1c5c39bdef3e"
        )[0].email, "abc@google.com")


if __name__ == '__main__':
    unittest.main()
