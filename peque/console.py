#!/usr/bin/python3
""" Class definition """
import cmd
from models.base_model import BaseModel
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand that inherits from cmd """
    prompt = '(hbnb) '

    def __init__(self):
        """Initializes"""
        cmd.Cmd.__init__(self)
        self.aliases = {
            'show': self.do_show,
            'h': self.do_help}

    def default(self, line):
        """Default"""
        arg = (line.replace('(', '.')).split('.')
        if len(arg) > 2 and arg[1] in self.aliases:
            self.aliases[arg[1]](f"{str(arg[0])} {str(arg[2])[:-1]}")
        else:
            print("*** Unknown syntax: %s" % line)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program"""
        return True

    def emptyline(self):
        """If a line is empty it does nothing"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if len(arg.split()) == 0:
            print("** class name missing **")
        else:
            try:
                new_instance = (eval(arg.split()[0]))()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the \
class name and id"""
        if len(arg.split()) == 0:
            print("** class name missing **")
            return
        elif len(arg.split()) > 0:
            try:
                eval(arg.split()[0])
            except NameError:
                print("** class doesn't exist **")
                return
        if len(arg.split()) < 2:
            print("** instance id missing **")
            return
        else:
            d = storage.all()
            if f"{arg.split()[0]}.{arg.split()[1]}" in d:
                print(d[f"{arg.split()[0]}.{arg.split()[1]}"])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
