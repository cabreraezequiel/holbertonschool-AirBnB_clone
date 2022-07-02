from models.base_model import BaseModel
from datetime import datetime
import unittest

class BaseModelTest(unittest.TestCase):

    def test_types(self):
        base_1 = BaseModel()
        self.assertIs(type(base_1.id), str)
        self.assertIs(type(base_1.created_at), datetime)
        self.assertIs(type(base_1.updated_at), datetime)

    @unittest.expectedFailure
    def test_unique_id(self):
        base_1 = BaseModel()
        base_2 = BaseModel()
        self.assertEqual(base_1.id(), base_2.id())
