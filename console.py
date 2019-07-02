#!/usr/bin/python3
""" module to create the console """
import cmd
import json
from shlex import split
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

    def do_destroy(self, args):
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
            del all_objs[obj_id]
            listm = {}
            for key, val in all_objs.items():
                listm.update({key: val.to_dict()})
            with open(storage._FileStorage__file_path, "w") as write_file:
                write_file.write(json.dumps(listm))
            return
        print("** no instance found **")

    def do_update(self, args):
        args = split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **'")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if obj_id.split(".")[1] != args[1]:
                continue
            setattr(all_objs[obj_id], args[2], args[3])
            listm = {}
            for key, val in all_objs.items():
                listm.update({key: val.to_dict()})
            with open(storage._FileStorage__file_path, "w") as write_file:
                write_file.write(json.dumps(listm))
            return
        print("** no instance found **")

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
