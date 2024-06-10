import os
import unittest
from unittest import TestCase
from models.user import User
from repository.user_db import UserDatabase


class TestUserDatabase(TestCase):
    """Test class for the UserDatabase class"""

    def setUp(self):
        """Setup method for the test class"""
        self.filename = "/home/walter_obrien/Documents/tutorials/python/oop_project/tests/test_user.csv"
        self.empty_filename = "/home/walter_obrien/Documents/tutorials/python/oop_project/tests/empty_user.csv"
        self.user = User(email="smith@google.com", name="Alex Smith")
        self.user.password = "AleSmi12344"

    def test_userdb_init_without_empty_file(self):
        """Test the UserDatabase constructor"""
        db = UserDatabase(self.filename)
        self.assertEqual(db._file, self.filename)
        self.assertGreater(os.path.getsize(self.filename), 0)

    def test_userdb_init_with_empty_file(self):
        """Test the UserDatabase constructor"""
        db = UserDatabase(self.empty_filename)
        self.assertEqual(db._file, self.empty_filename)
        self.assertEqual(os.path.getsize(self.empty_filename), 0)

    def test_userdb_init_with_none_file(self):
        """Test the UserDatabase constructor"""
        with self.assertRaises(ValueError):
            UserDatabase(None)

    def test_userdb_add_method(self):
        """Test add method for UserDatabase
        """
        db = UserDatabase(self.filename)
        self.assertIsInstance(db.add(self.user), User)

    def test_userdb_add_method_with_invalid_data(self):
        """Test add method for UserDatabase
        """
        db = UserDatabase(self.filename)
        with self.assertRaises(ValueError):
            db.add(None)

    def test_userdb_add_method_with_empty_file(self):
        """Test add method for UserDatabase
        """
        db = UserDatabase(self.empty_filename)
        self.assertIsInstance(db.add(self.user), User)

    def test_userdb_add_method_with_invalid_data_type(self):
        """Test add method for UserDatabase
        """
        db = UserDatabase(self.filename)
        with self.assertRaises(TypeError):
            db.add("user")

    def test_userdb_add_method_with_invalid_data_type_in_empty_file(self):
        """Test add method for UserDatabase
        """
        db = UserDatabase(self.empty_filename)
        with self.assertRaises(TypeError):
            db.add("user")

    def test_userdb_all_method(self):
        """Test all method for UserDatabase
        """
        db = UserDatabase(self.filename)
        all_users = db.all()
        self.assertEqual(next(all_users).email, "abc@google.com")
        self.assertEqual(next(all_users).email, "someone@example.com")
        with self.assertRaises(StopIteration):
            next(all_users)

    def test_userdb_update_method(self):
        """Test update method for UserDatabase
        """
        db = UserDatabase(self.filename)
        item = {"name": "Austin Black"}
        self.assertIsInstance(
            db.update(id="835f2634-68ee-4e00-8144-c0210f8ef175", item=item), User)

    def test_userdb_update_method_with_invalid_data(self):
        """Test update method for UserDatabase
        """
        db = UserDatabase(self.filename)
        with self.assertRaises(ValueError):
            db.update(id="835f2634-68ee-4e00-8144-c0210f8ef175", item=None)

        with self.assertRaises(TypeError):
            db.update(id="835f2634-68ee-4e00-8144-c0210f8ef175", item="item")

    def test_userdb_get_method(self):
        """Test get method for UserDatabase
        """
        db = UserDatabase(self.filename)
        self.assertIsInstance(
            db.get("835f2634-68ee-4e00-8144-c0210f8ef175")[0], User)
        self.assertEqual(db.get("835f2634-68ee-4e00-8144-c0210f8ef175")[0].email, "abc@google.com")

    def test_userdb_get_method_with_invalid_data(self):
        """Test get method for UserDatabase
        """
        db = UserDatabase(self.filename)
        self.assertIsNone(db.get("835f2634-68ee-4e00-8144-c0210f8ef174"))

    def test_userdb_delete_method(self):
        """Test delete method for UserDatabase
        """
        db = UserDatabase(self.filename)
        self.assertIsNone(
            db.delete("835f2634-68ee-4e00-8144-c0210f8ef175"))

    def test_userdb_delete_method_with_invalid_data(self):
        """Test delete method for UserDatabase
        """
        db = UserDatabase(self.filename)
        with self.assertRaises(ValueError):
            db.delete("835f2634-68ee-4e00-8144-c0210f8ef174")

    def test_userdb_delete_method_with_invalid_data_type(self):
        """Test delete method for UserDatabase
        """
        db = UserDatabase(self.filename)
        with self.assertRaises(ValueError):
            db.delete(None)

    def test_userdb_save_method(self):
        """Test save method for UserDatabase
        """
        db = UserDatabase(self.filename)
        db.add(self.user)
        self.assertIsNone(db.save())
        with open(self.filename, "r") as file:
            self.assertEqual(len(file.readlines()), 4)

if __name__ == '__main__':
    unittest.main()
