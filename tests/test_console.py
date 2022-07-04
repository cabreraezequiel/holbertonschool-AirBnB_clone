from console import HBNBCommand
import re
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
        self.assertEqual(f.getvalue(), "")

    def test_help(self):
        """ Test EOF command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        self.assertTrue(f)
        self.assertIsNotNone(f.getvalue())
        self.assertNotEqual(f.getvalue(), "")
        self.assertEqual(f.getvalue(), "\nDocumented commands (type help \
<topic>):\n========================================\nEOF  all  count  create\
  destroy  help  quit  show  update\n\n")
        with patch('sys.stdout', new=StringIO()) as f_1:
            HBNBCommand().onecmd("help show")
        self.assertTrue(f_1)
        self.assertIsNotNone(f_1)
        self.assertNotEqual(f_1.getvalue(), "")
        self.assertEqual(f_1.getvalue(), "Prints the string representation of \
an instance based on the class name and id. Usage: \033[92mshow <class name> \
<id>\33[0m or \033[92m<class name>.show(<id>)\33[0m\n""")

    def test_emptyline(self):
        """ Test empty line """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
        self.assertEqual(f.getvalue(), "")

    def test_createBaseModel(self):
        """ Test create BaseModel """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        self.assertNotEqual(f.getvalue(), "")
        self.assertIsNotNone(f.getvalue())
