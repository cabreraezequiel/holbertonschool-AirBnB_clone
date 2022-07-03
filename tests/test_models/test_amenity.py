from models.amenity import Amenity
import unittest
"""Tests for Amenity class"""


class AmenityTest(unittest.TestCase):
    """Unittests for Amenity"""

    def test_types(self):
        """ Test type of attributes"""
        amenity_1 = Amenity()
        self.assertIs(type(Amenity.name), str)

    def test_attributes(self):
        """ Test attributes of Amenity class"""
        amenity_1 = Amenity()
        self.assertEqual(amenity_1.name, "")
        amenity_1.name = "test"
        self.assertEqual(amenity_1.name, "test")

    def test_to_dict(self):
        """ Test to_dict() method"""
        amenity_1 = Amenity()
        amenity_1.name = "test"
        self.assertIn('__class__', amenity_1.to_dict())
        self.assertIn('id', amenity_1.to_dict())
        self.assertIn('created_at', amenity_1.to_dict())
        self.assertIn('updated_at', amenity_1.to_dict())
        self.assertIn('name', amenity_1.to_dict())
