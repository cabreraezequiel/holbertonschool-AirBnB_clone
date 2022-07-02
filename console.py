#!/usr/bin/python3
""" Class definition """
import cmd
import re
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
    prompt = '(hbnb)'

#    def __init__(self):
#        """Initializes"""
#        cmd.Cmd.__init__(self)
#        self.aliases = {
#            'show': self.do_show,
#            'count': self.do_count}

#    def default(self, line):
#        """Default"""
##       arg = (line.replace('(', '.')).split('.')
#        pattern = r"[(.)]"
#        arg = re.split(pattern, line)
##        print(arg)
#        if len(arg) > 3 and arg[1] in self.aliases:
#            self.aliases[arg[1]](f"{str(arg[0])} {str(arg[2])}")
#        else:
#            print("*** Unknown syntax: %s" % line)

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
        """Creates a new instance of BaseModel, saves it and prints the id. Usage create \33[31m<class name>\33[30m"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            try:
                new_instance = (eval(args[0]))()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the \
class name and id. Usage \33[31mshow <class name> <id>\33[0m or \33[31m<class \
name>.show(<id>)\33[0m"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) > 0:
            try:
                eval(args[0])
            except NameError:
                print("** class doesn't exist **")
                return
        if len(args) < 2:
            print("** instance id missing **")
            return
        else:
            dic = storage.all()
#            print(dic)
#            print(f"{arg.split()[0]}.{arg.split()[1]}")
            if f"{arg.split()[0]}.{arg.split()[1]}" in dic:
                print(dic[f"{arg.split()[0]}.{arg.split()[1]}"])
            else:
                print("** no instance found **")

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        if len(arg.split()) == 0:
            print("** class name missing **")
            return
        elif len(arg.split()) > 0:
            try:
                eval(arg.split()[0])
            except NameError:
                print("** class doesn't exist **")
                return
        if len(arg.split()) < 1:
            print("** instance id missing **")
            return
        else:
            count = 0
            d = storage.all()
            for key in d:
                if f"{str(arg.split()[0])}" in key:
                    count += 1
            print(count)

#    def do_all(self, arg):
#        """Retrieve the number of instances of a class"""
#        if len(arg.split()) == 0:
#            dic = storage.all()
#            for key in dic:
#                print(dic[key].__repr__(), end="")
#            return
#        elif len(arg.split()) > 0:
#            try:
#                eval(arg.split()[0])
#            except NameError:
#                print("** class doesn't exist **")
#                return
#        if len(arg.split()) < 1:
#            print("** instance id missing **")
#            return
#        else:
#            count = 0
#            d = storage.all()
#            for key in d:
#                if f"{str(arg.split()[0])}" in key:
#                    count += 1
#            print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
