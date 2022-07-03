from models.engine.file_storage import FileStorage
from models.user import User
import unittest
"""Tests for FileStorage class"""


class FileStorageTest(unittest.TestCase):
    """Unittests for FileStorage"""

    @classmethod
    def setUpClass(self):
        """ For test use """
        self.user_2 = User()

    def test_types(self):
        """ Test type of attributes"""
        storage_1 = FileStorage()
        self.assertIs(type(storage_1.all()), dict)
        self.assertIs(type(storage_1._FileStorage__objects), dict)
        self.assertIs(type(storage_1._FileStorage__file_path), str)

    def test_all(self):
        """ Test all method of FileStorage class"""
        storage_1 = FileStorage()
        self.assertEqual(storage_1.all(), storage_1._FileStorage__objects)
        self.assertEqual(storage_1._FileStorage__file_path, "file.json")

    def test_save(self):
        """ Test save method of FileStorage class"""
        user_1 = User()
        storage = FileStorage()
        self.assertNotIn(user_1.id, storage.all())
        storage.new(user_1)
        self.assertIn(f"User.{user_1.id}", storage.all().keys())

    def test_save(self):
        """ Test reload method of FileStorage class"""
        storage_1 = FileStorage()
        storage_2 = FileStorage()
        storage_1.new(self.user_2)
        storage_1.save()
        self.assertIn(f"User.{self.user_2.id}", storage_1.all().keys())
        self.assertIn(f"User.{self.user_2.id}", storage_2.all().keys())

    def test_reload(self):
        """ Test reload method of FileStorage class"""
        storage_1 = FileStorage()
        storage_1.reload()
        self.assertIn(f"User.{self.user_2.id}", storage_1.all().keys())
