#!/usr/bin/python3
""" Class definition """
import cmd
import re
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand that inherits from cmd """
    prompt = '(hbnb) '

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
        """Creates a new instance of BaseModel, saves it and prints the id. \
Usage: \033[92mcreate <class name>\033[0m"""

        if len(arg.split()) == 0:
            print("** class name missing **")
        else:
            try:
                new_instance = storage.classes()[arg.split()[0]]()
                new_instance.save()
                print(new_instance.id)
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the \
class name and id. Usage: \033[92mshow <class name> <id>\33[0m or \033[92m<\
class name>.show(<id>)\33[0m"""

        if len(arg.split()) == 0:
            print("** class name missing **")
        elif arg.split()[0] not in storage.classes():
             print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        else:
            dic = storage.all()
            if f"{arg.split()[0]}.{arg.split()[1]}" in dic:
                print(dic[f"{arg.split()[0]}.{arg.split()[1]}"])
            else:
                print("** no instance found **")

    def do_count(self, arg):
        """Retrieves the number of instances of a class. Usage: \033[92mcount \
<class name>\33[0m or \033[92m<class name>.count()\33[0m"""
        if len(arg.split()) == 0:
            print("** class name missing **")
        elif arg.split()[0] not in storage.classes():
             print("** class doesn't exist **")
        else:
            count = 0
            for v in storage.all().values():
                if arg.split()[0] == v.__class__.__name__:
                    count += 1
            print(count)

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on \
the class name. Usage: \033[92mall \033[91m<class name>\33[0m or \033[92m<\
class name>.all\33[0m --\033[91m[OPTIONAL]\33[0m"""

        dic = []
        if len(arg.split()) < 1:
            for value in storage.all().values():
                dic.append(str(value))
            print(dic)
        elif arg.split()[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            for value in storage.all().values():
                if arg.split()[0] == value.__class__.__name__:
                    dic.append(str(value))
            print(dic)

    def precmd(self, line):
        """Changes input"""
        pattern = r"[(.)]"
        arg = re.split(pattern, line)
        if len(arg) > 3:# and func[arg[1]]:
            line = (f"{str(arg[1])} {str(arg[0])} {str(arg[2])}")
        return cmd.Cmd.precmd(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
