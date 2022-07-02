from models.base_model import BaseModel
import unittest
from model.base_model import BaseModel

class BaseModelTest(unittest.TestCase):
    test1 = BaseModel()
    def test_0(self):
        self.assertTrue(True)
    def fun_not_run(self):
        print("no run")
