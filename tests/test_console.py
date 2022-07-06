from console import HBNBCommand
import re
import sys
import unittest
from unittest.mock import patch
from io import StringIO
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.base_model import BaseModel
from models.user import User
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
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create test")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_showBaseModel(self):
        """ Test create BaseModel """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        obj_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show test")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 123")
        self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {obj_id}")
        self.assertIn(f"[BaseModel] ({obj_id[:-1]})", f.getvalue())

    def test_destroyBaseModel(self):
        """ Test destroy BaseModel """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        obj_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy test")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 123")
        self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel {obj_id}")
        self.assertEqual(f.getvalue(), "")
        self.assertNotIn(f"[BaseModel] ({obj_id[:-1]})", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {obj_id}")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_all(self):
        """ Test all command """
        base_1 = BaseModel()
        place_1 = Place()
        place_2 = Place()
        user_1 = User()
        state_1 = State()
        amenity_1 = Amenity()
        review_1 = Review()
        city_1 = City()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        self.assertIn(f"[BaseModel] ({base_1.id})", f.getvalue())
        self.assertIn(f"[Place] ({place_1.id})", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all test")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
        self.assertIn(f"[BaseModel] ({base_1.id})", f.getvalue())
        self.assertNotIn(f"[Place] ({place_1.id})", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Place")
        self.assertIn(f"[Place] ({place_1.id})", f.getvalue())
        self.assertIn(f"[Place] ({place_2.id})", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
        self.assertIn(f"[BaseModel] ({base_1.id})", f.getvalue())
        self.assertNotIn(f"[Place] ({place_1.id})", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
        self.assertIn(f"[Place] ({place_1.id})", f.getvalue())
        self.assertIn(f"[Place] ({place_2.id})", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
        self.assertIn(f"[User] ({user_1.id})", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.all()")
        self.assertIn(f"[Review] ({review_1.id})", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
        self.assertIn(f"[State] ({state_1.id})", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
        self.assertIn(f"[City] ({city_1.id})", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
        self.assertIn(f"[Amenity] ({amenity_1.id})", f.getvalue())

    def test_count(self):
        """ Test count command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
        counter = str(int(f.getvalue()) + 1)
        base_1 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
        self.assertEqual(f.getvalue(), counter + '\n')
        place_1 = Place()
        place_2 = Place()
        user_1 = User()
        state_1 = State()
        amenity_1 = Amenity()
        review_1 = Review()
        city_1 = City()
