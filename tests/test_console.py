from console import HBNBCommand
import sys
import unittest
from unittest.mock import patch
from io import StringIO
"""Tests for console"""


class HBNBCommandTest(unittest.TestCase):
    """Unittests for HBNBCommand"""

    def test_quit(self):
        """ Test quit command """
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("quit")
        self.assertTrue(f)
        self.assertEqual(f.getvalue(), "")

    def test_EOF(self):
        """ Test EOF command """
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("EOF")
        self.assertTrue(f)

    def test_help(self):
        """ Test EOF command """
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help")
        self.assertTrue(f)
        self.assertIsNotNone(f.getvalue())
        self.assertNotEqual(f.getvalue(), "")
        with patch('sys.stdout', new=StringIO()) as f_1:
                HBNBCommand().onecmd("help show")
        self.assertTrue(f_1)
        self.assertIsNotNone(f_1)
        self.assertNotEqual(f_1.getvalue(), "")
