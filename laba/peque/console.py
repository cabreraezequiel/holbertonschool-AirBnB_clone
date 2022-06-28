#!/usr/bin/python3
""" Class definition """
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand that inherits from cmd """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """EOF to exit the program"""
        exit()

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
        """Prints the string representation of an instance based on the class name and id"""
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
