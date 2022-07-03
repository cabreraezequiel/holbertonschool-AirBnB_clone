from models.state import State
import unittest
"""Tests for State class"""


class StateTest(unittest.TestCase):
    """Unittests for State"""

    def test_types(self):
        """ Test type of attributes"""
        state_1 = State()
        self.assertIs(type(State.name), str)

    def test_attributes(self):
        """ Test attributes of State class"""
        state_1 = State()
        self.assertEqual(state_1.name, "")
        state_1.name = "test"
        self.assertEqual(state_1.name, "test")

    def test_to_dict(self):
        """ Test to_dict() method"""
        state_1 = State()
        state_1.state = "test"
        self.assertIn('__class__', state_1.to_dict())
        self.assertIn('id', state_1.to_dict())
        self.assertIn('created_at', state_1.to_dict())
        self.assertIn('updated_at', state_1.to_dict())
        self.assertIn('state', state_1.to_dict())
