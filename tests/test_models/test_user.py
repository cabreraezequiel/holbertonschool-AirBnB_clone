from models.user import User
import unittest
"""Tests for User class"""


class UserTest(unittest.TestCase):
    """Unittests for User"""

    def test_types(self):
        """ Test type of attributes"""
        user_1 = User()
        self.assertIs(type(User.password), str)
        self.assertIs(type(User.email), str)
        self.assertIs(type(User.first_name), str)
        self.assertIs(type(User.last_name), str)

    def test_attributes(self):
        """ Test attributes of User class"""
        user_1 = User()
        self.assertEqual(user_1.__str__(),
                         f"[User] ({user_1.id}) {user_1.__dict__}")
        self.assertEqual(user_1.email, "")
        self.assertEqual(user_1.password, "")
        self.assertEqual(user_1.first_name, "")
        self.assertEqual(user_1.last_name, "")
        user_1.email = "test"
        user_1.password = "test"
        user_1.first_name = "test"
        user_1.last_name = "test"
        self.assertEqual(user_1.email, "test")
        self.assertEqual(user_1.password, "test")
        self.assertEqual(user_1.first_name, "test")
        self.assertEqual(user_1.last_name, "test")

    def test_to_dict(self):
        """ Test to_dict() method"""
        user_1 = User()
        user_1.email = "test"
        user_1.password = "test"
        user_1.first_name = "test"
        user_1.last_name = "test"
        self.assertIs(type(user_1.to_dict()), dict)
        self.assertIn('__class__', user_1.to_dict())
        self.assertIn('id', user_1.to_dict())
        self.assertIn('created_at', user_1.to_dict())
        self.assertIn('updated_at', user_1.to_dict())
        self.assertIn('email', user_1.to_dict())
        self.assertIn('password', user_1.to_dict())
        self.assertIn('first_name', user_1.to_dict())
        self.assertIn('last_name', user_1.to_dict())
