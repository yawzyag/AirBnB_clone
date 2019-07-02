#!/usr/bin/python3
""" module to create the console """
import cmd
import json
from shlex import split
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Command processor for HBNB\n """
    strclasses = ["BaseModel", "State", "City",
                  "Amenity", "Review", "Place", "User"]

    def do_create(self, args):
        """ Creates a new instance of BaseModel\n """
        if len(args) == 0:
            print("** class name missing **")
            return
        if args not in self.strclasses:
            print("** class doesn't exist **")
            return
        if args == self.strclasses[0]:
            my_model = BaseModel()
        elif args == self.strclasses[1]:
            my_model = State()
        elif args == self.strclasses[2]:
            my_model = City()
        elif args == self.strclasses[3]:
            my_model = Amenity()
        elif args == self.strclasses[4]:
            my_model = Review()
        elif args == self.strclasses[5]:
            my_model = Place()
        my_model.save()
        print(my_model.id)

    def do_show(self, args):
        """ Prints the string representation of an instance\n """
        if len(args) == 0:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in self.strclasses:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            splitted = obj_id.split(".")
            if splitted[1] != args[1] or splitted[0] != args[0]:
                continue
            obj = all_objs[obj_id]
            print(obj)
            return
        print("** no instance found **")

    def do_all(self, args):
        """ Prints all string representation of all instances\n """
        if args not in self.strclasses and len(args) > 0:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if len(args) > 0:
                if obj_id.split(".")[0] != args:
                    continue
            obj = all_objs[obj_id]
            print(obj)

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id\n """
        if len(args) == 0:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in self.strclasses:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            splitted = obj_id.split(".")
            if splitted[1] != args[1] or splitted[0] != args[0]:
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
        """ Update an instance of a class\n """
        args = split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.strclasses:
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
            splitted = obj_id.split(".")
            if splitted[1] != args[1] or splitted[0] != args[0]:
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
        """ Quit manage empty line\n """
        return

    def do_EOF(self, line):
        """Exit\n"""
        return True

    def do_quit(self, line):
        """ Quit command to exit the program\n """
        return True


if __name__ == '__main__':
    """ should not be executed when imported """
    HBNBCommand.prompt = "(hbnb) "
    HBNBCommand().cmdloop()
