#!/usr/bin/python3
""" module to create the console """
import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_show(self, args):
        if len(args) == 0:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if obj_id.split(".")[1] != args[1]:
                continue
            obj = all_objs[obj_id]
            print(obj)
            return
        print("** no instance found **")

    def do_all(self, args):
        if args != "BaseModel" and len(args) > 0:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)

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
