#!/usr/bin/python3
""" Class definition """
import cmd
import uuid
import datetime


class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand that inherits from cmd """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """EOF to exit the program"""
        exit()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
