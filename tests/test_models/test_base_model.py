from models.base_model import BaseModel
import unittest
from datetime import datetime
"""Test Module for BaseModel class"""


class BaseModelTest(unittest.TestCase):
    """Test_class for BaseModel"""
    def test_types(self):
        """Test the Type is correct"""
        base_1 = BaseModel()
        self.assertIs(type(base_1.id), str)
        self.assertIs(type(base_1.created_at), datetime)
        self.assertIs(type(base_1.updated_at), datetime)

    def test_unique_id(self):
        """Tasts the id is unique"""
        base_1 = BaseModel()
        base_2 = BaseModel()
        test_id = base_2.id
        self.assertNotEqual(base_1.id, base_2.id)
        self.assertEqual(base_2.id, test_id)

    def test_str(self):
        """Tests the __str__ method"""
        base_1 = BaseModel()
        self.assertEqual(base_1.__str__(),
                         f"[BaseModel] ({base_1.id}) {base_1.__dict__}")

    def test_save(self):
        """Tests saving method"""
        base_1 = BaseModel()
        update = base_1.updated_at
        self.assertEqual(base_1.updated_at, update)
        base_1.save()
        self.assertNotEqual(base_1.updated_at, update)

    def test_to_dict(self):
        """Tests setting instances into dictionary for JSON serialization"""
        base_1 = BaseModel()
        self.assertIs(type(base_1.to_dict()), dict)
        self.assertIn('__class__', base_1.to_dict())
        self.assertIn('id', base_1.to_dict())
        self.assertIn('created_at', base_1.to_dict())
        self.assertIn('updated_at', base_1.to_dict())
