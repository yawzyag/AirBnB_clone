#!/usr/bin/python3
""" module to create the console """
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    "Command processor for HBNB\n"

    def do_create(self, args):
        if len(args) == 0:
            print("** class name missing **")
            return
        if args != "BaseModel":
            print("** class doesn't exist **")
            return
        my_model = BaseModel()
        my_model.save()
        print(my_model.id)

    def emptyline(self):
        return

    def do_EOF(self, line):
        "Exit\n"
        return True

    def do_quit(self, line):
        "Quit command to exit the program\n"
        return True


if __name__ == '__main__':
    HBNBCommand.prompt = "(hbnb) "
    HBNBCommand().cmdloop()
