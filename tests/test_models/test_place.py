from models.place import Place
import unittest
"""Tests for Place class"""


class PlaceTest(unittest.TestCase):
    """Unittests for Place"""

    def test_types(self):
        """ Test type of attributes"""
        place_1 = Place()
        self.assertIs(type(Place.name), str)
        self.assertIs(type(Place.city_id), str)
        self.assertIs(type(Place.user_id), str)
        self.assertIs(type(Place.description), str)
        self.assertIs(type(Place.number_rooms), int)
        self.assertIs(type(Place.number_bathrooms), int)
        self.assertIs(type(Place.max_guest), int)
        self.assertIs(type(Place.price_by_night), int)
        self.assertIs(type(Place.latitude), float)
        self.assertIs(type(Place.longitude), float)
        self.assertIs(type(Place.amenity_ids), list)

    def test_attributes(self):
        """ Test attributes of Place class"""
        place_1 = Place()
        self.assertEqual(place_1.name, "")
        self.assertEqual(place_1.city_id, "")
        self.assertEqual(place_1.user_id, "")
        self.assertEqual(place_1.description, "")
        self.assertEqual(place_1.number_rooms, 0)
        self.assertEqual(place_1.number_bathrooms, 0)
        self.assertEqual(place_1.max_guest, 0)
        self.assertEqual(place_1.price_by_night, 0)
        self.assertEqual(place_1.latitude, 0.0)
        self.assertEqual(place_1.longitude, 0.0)
        self.assertEqual(place_1.amenity_ids, [])
        place_1.name = "test"
        place_1.city_id = "test"
        place_1.user_id = "test"
        place_1.description = "test"
        place_1.number_rooms = 1
        place_1.number_bathrooms = 1
        place_1.max_guest = 1
        place_1.price_by_night = 1
        place_1.latitude = 1.0
        place_1.longitude = 1.0
        place_1.amenity_ids = ["test"]
        self.assertEqual(place_1.name, "test")
        self.assertEqual(place_1.city_id, "test")
        self.assertEqual(place_1.user_id, "test")
        self.assertEqual(place_1.description, "test")
        self.assertEqual(place_1.number_rooms, 1)
        self.assertEqual(place_1.number_bathrooms, 1)
        self.assertEqual(place_1.max_guest, 1)
        self.assertEqual(place_1.price_by_night, 1)
        self.assertEqual(place_1.latitude, 1.0)
        self.assertEqual(place_1.longitude, 1.0)
        self.assertEqual(place_1.amenity_ids, ["test"])

    def test_to_dict(self):
        """ Test to_dict() method"""
        place_1 = Place()
        place_1.name = "test"
        place_1.city_id = "test"
        place_1.user_id = "test"
        place_1.description = "test"
        place_1.number_rooms = 1
        place_1.number_bathrooms = 1
        place_1.max_guest = 1
        place_1.price_by_night = 1
        place_1.latitude = 1.0
        place_1.longitude = 1.0
        place_1.amenity_ids = ["test"]
        self.assertIn('__class__', place_1.to_dict())
        self.assertIn('id', place_1.to_dict())
        self.assertIn('created_at', place_1.to_dict())
        self.assertIn('updated_at', place_1.to_dict())
        self.assertIn('name', place_1.to_dict())
        self.assertIn('user_id', place_1.to_dict())
        self.assertIn('city_id', place_1.to_dict())
        self.assertIn('description', place_1.to_dict())
        self.assertIn('number_rooms', place_1.to_dict())
        self.assertIn('number_bathrooms', place_1.to_dict())
        self.assertIn('max_guest', place_1.to_dict())
        self.assertIn('price_by_night', place_1.to_dict())
        self.assertIn('latitude', place_1.to_dict())
        self.assertIn('longitude', place_1.to_dict())
        self.assertIn('amenity_ids', place_1.to_dict())
