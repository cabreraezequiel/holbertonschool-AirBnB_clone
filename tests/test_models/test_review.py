from models.review import Review
import unittest
"""Tests for Review class"""


class ReviewTest(unittest.TestCase):
    """Unittests for Review"""

    def test_types(self):
        """ Test type of attributes"""
        review_1 = Review()
        self.assertIs(type(Review.place_id), str)
        self.assertIs(type(Review.user_id), str)
        self.assertIs(type(Review.text), str)

    def test_attributes(self):
        """ Test attributes of Review class"""
        review_1 = Review()
        self.assertEqual(review_1.place_id, "")
        self.assertEqual(review_1.user_id, "")
        self.assertEqual(review_1.text, "")
        review_1.place_id = "test"
        review_1.user_id = "test"
        review_1.text = "test"
        self.assertEqual(review_1.place_id, "test")
        self.assertEqual(review_1.user_id, "test")
        self.assertEqual(review_1.text, "test")

    def test_to_dict(self):
        """ Test to_dict() method"""
        review_1 = Review()
        review_1.place_id = "test"
        review_1.user_id = "test"
        review_1.text = "test"
        self.assertIn('__class__', review_1.to_dict())
        self.assertIn('id', review_1.to_dict())
        self.assertIn('created_at', review_1.to_dict())
        self.assertIn('updated_at', review_1.to_dict())
        self.assertIn('place_id', review_1.to_dict())
        self.assertIn('user_id', review_1.to_dict())
        self.assertIn('text', review_1.to_dict())
