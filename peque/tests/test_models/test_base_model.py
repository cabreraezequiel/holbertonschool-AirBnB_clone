from models.base_model import BaseModel
import unittest

class TestFoo(unittest.TestCase):
    test1 = BaseModel()
    def test_foo(self):
        self.assertTrue(True)
    def fun_not_run(self):
        print("no run")
