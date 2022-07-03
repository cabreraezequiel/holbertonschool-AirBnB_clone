from models.city import City
import unittest
"""Tests for City class"""


class CityTest(unittest.TestCase):
    """Unittests for City"""

    def test_types(self):
        """ Test type of attributes"""
        city_1 = City()
        self.assertIs(type(City.name), str)
	self.assertIs(type(City.state_id), str)

    def test_attributes(self):
        """ Test attributes of City class"""
        city_1 = City()
        self.assertEqual(city_1.name, "")
        self.assertEqual(city_1.state_id, "")
        city_1.name = "test"
        city_1.state_id = "test"
        self.assertEqual(city_1.name, "test")
        self.assertEqual(city_1.state_id, "test")

    def test_to_dict(self):
        """ Test to_dict() method"""
        city_1 = City()
        city_1.name = "test"
        city_1.state_id = "test"
        self.assertIn('__class__', city_1.to_dict())
        self.assertIn('id', city_1.to_dict())
        self.assertIn('created_at', city_1.to_dict())
        self.assertIn('updated_at', city_1.to_dict())
        self.assertIn('name', city_1.to_dict())
        self.assertIn('state_id', city_1.to_dict())
