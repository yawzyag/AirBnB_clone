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
from models.user import User
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
        elif args == self.strclasses[6]:
            my_model = User()
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
        obj = []
        for obj_id in all_objs.keys():
            if len(args) > 0:
                if obj_id.split(".")[0] != args:
                    continue
            obj.append(str(all_objs[obj_id]))
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
            print("** class doesn't exist **")
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
            if (args[3][-1] != "\"" and not args[3].isalpha() and
                    " " not in args[3] and "_" not in args[3]):
                if "." in args[3]:
                    args[3] = float(args[3])
                else:
                    args[3] = int(args[3])
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

    def do_User(self, line):
        if line == ".all()":
            HBNBCommand().do_all("User")
        if line == ".count()":
            all_objs = storage.all()
            contar = 0
            for obj_id in all_objs.keys():
                if obj_id.split(".")[0] != "User":
                    continue
                contar += 1
            print(contar)
        if line[0:6] == ".show(" and line[-1] == ")":
            HBNBCommand().do_show("User " + line[7:-2])
        if line[0:9] == ".destroy(" and line[-1] == ")":
            HBNBCommand().do_destroy("User " + line[10:-2])
        if line[0:8] == ".update(" and line[-1] == ")":
            if line[-2] != "}":
                str1 = line[8:-1]
                str1 = "".join(str1.split(","))
                HBNBCommand().do_update("User " + str1)
            else:
                str1 = line[8:-1]
                str1 = str1.split(",")
                str2 = str1[0]
                del str1[0]
                dict1 = eval(",".join(str1))
                for i, j in dict1.items():
                    str3 = " \"" + i + "\" "
                    if type(j) is str:
                        str4 = "\"" + j + "\""
                        HBNBCommand().do_update("User " + str2 + str3 + str4)
                    else:
                        HBNBCommand().do_update("User " + str2 + str3 + str(j))

    def do_Place(self, line):
        if line == ".all()":
            HBNBCommand().do_all("Place")
        if line == ".count()":
            all_objs = storage.all()
            contar = 0
            for obj_id in all_objs.keys():
                if obj_id.split(".")[0] != "Place":
                    continue
                contar += 1
            print(contar)
        if line[0:6] == ".show(" and line[-1] == ")":
            HBNBCommand().do_show("Place " + line[7:-2])
        if line[0:9] == ".destroy(" and line[-1] == ")":
            HBNBCommand().do_destroy("Place " + line[10:-2])
        if line[0:8] == ".update(" and line[-1] == ")":
            if line[-2] != "}":
                str1 = line[8:-1]
                str1 = "".join(str1.split(","))
                HBNBCommand().do_update("Place " + str1)
            else:
                str1 = line[8:-1]
                str1 = str1.split(",")
                str2 = str1[0]
                del str1[0]
                dict1 = eval(",".join(str1))
                for i, j in dict1.items():
                    str3 = " \"" + i + "\" "
                    if type(j) is str:
                        str4 = "\"" + j + "\""
                        HBNBCommand().do_update("Place " + str2 + str3 + str4)
                    else:
                        HBNBCommand().do_update("Place " +
                                                str2 + str3 + str(j))

    def do_State(self, line):
        if line == ".all()":
            HBNBCommand().do_all("State")
        if line == ".count()":
            all_objs = storage.all()
            contar = 0
            for obj_id in all_objs.keys():
                if obj_id.split(".")[0] != "State":
                    continue
                contar += 1
            print(contar)
        if line[0:6] == ".show(" and line[-1] == ")":
            HBNBCommand().do_show("State " + line[7:-2])
        if line[0:9] == ".destroy(" and line[-1] == ")":
            HBNBCommand().do_destroy("State " + line[10:-2])
        if line[0:8] == ".update(" and line[-1] == ")":
            if line[-2] != "}":
                str1 = line[8:-1]
                str1 = "".join(str1.split(","))
                HBNBCommand().do_update("State " + str1)
            else:
                str1 = line[8:-1]
                str1 = str1.split(",")
                str2 = str1[0]
                del str1[0]
                dict1 = eval(",".join(str1))
                for i, j in dict1.items():
                    str3 = " \"" + i + "\" "
                    if type(j) is str:
                        str4 = "\"" + j + "\""
                        HBNBCommand().do_update("State " +
                                                str2 + str3 + str4)
                    else:
                        HBNBCommand().do_update("State " +
                                                str2 + str3 + str(j))

    def do_City(self, line):
        if line == ".all()":
            HBNBCommand().do_all("City")
        if line == ".count()":
            all_objs = storage.all()
            contar = 0
            for obj_id in all_objs.keys():
                if obj_id.split(".")[0] != "City":
                    continue
                contar += 1
            print(contar)
        if line[0:6] == ".show(" and line[-1] == ")":
            HBNBCommand().do_show("City " + line[7:-2])
        if line[0:9] == ".destroy(" and line[-1] == ")":
            HBNBCommand().do_destroy("City " + line[10:-2])
        if line[0:8] == ".update(" and line[-1] == ")":
            if line[-2] != "}":
                str1 = line[8:-1]
                str1 = "".join(str1.split(","))
                HBNBCommand().do_update("City " + str1)
            else:
                str1 = line[8:-1]
                str1 = str1.split(",")
                str2 = str1[0]
                del str1[0]
                dict1 = eval(",".join(str1))
                for i, j in dict1.items():
                    str3 = " \"" + i + "\" "
                    if type(j) is str:
                        str4 = "\"" + j + "\""
                        HBNBCommand().do_update("City " +
                                                str2 + str3 + str4)
                    else:
                        HBNBCommand().do_update("City " +
                                                str2 + str3 + str(j))

    def do_Amenity(self, line):
        if line == ".all()":
            HBNBCommand().do_all("Amenity")
        if line == ".count()":
            all_objs = storage.all()
            contar = 0
            for obj_id in all_objs.keys():
                if obj_id.split(".")[0] != "Amenity":
                    continue
                contar += 1
            print(contar)
        if line[0:6] == ".show(" and line[-1] == ")":
            HBNBCommand().do_show("Amenity " + line[7:-2])
        if line[0:9] == ".destroy(" and line[-1] == ")":
            HBNBCommand().do_destroy("Amenity " + line[10:-2])
        if line[0:8] == ".update(" and line[-1] == ")":
            if line[-2] != "}":
                str1 = line[8:-1]
                str1 = "".join(str1.split(","))
                HBNBCommand().do_update("Amenity " + str1)
            else:
                str1 = line[8:-1]
                str1 = str1.split(",")
                str2 = str1[0]
                del str1[0]
                dict1 = eval(",".join(str1))
                for i, j in dict1.items():
                    str3 = " \"" + i + "\" "
                    if type(j) is str:
                        str4 = "\"" + j + "\""
                        HBNBCommand().do_update("Amenity " +
                                                str2 + str3 + str4)
                    else:
                        HBNBCommand().do_update("Amenity " +
                                                str2 + str3 + str(j))

    def do_Review(self, line):
        if line == ".all()":
            HBNBCommand().do_all("Review")
        if line == ".count()":
            all_objs = storage.all()
            contar = 0
            for obj_id in all_objs.keys():
                if obj_id.split(".")[0] != "Review":
                    continue
                contar += 1
            print(contar)
        if line[0:6] == ".show(" and line[-1] == ")":
            HBNBCommand().do_show("Review " + line[7:-2])
        if line[0:9] == ".destroy(" and line[-1] == ")":
            HBNBCommand().do_destroy("Review " + line[10:-2])
        if line[0:8] == ".update(" and line[-1] == ")":
            if line[-2] != "}":
                str1 = line[8:-1]
                str1 = "".join(str1.split(","))
                HBNBCommand().do_update("Review " + str1)
            else:
                str1 = line[8:-1]
                str1 = str1.split(",")
                str2 = str1[0]
                del str1[0]
                dict1 = eval(",".join(str1))
                for i, j in dict1.items():
                    str3 = " \"" + i + "\" "
                    if type(j) is str:
                        str4 = "\"" + j + "\""
                        HBNBCommand().do_update("Review " +
                                                str2 + str3 + str4)
                    else:
                        HBNBCommand().do_update("Review " +
                                                str2 + str3 + str(j))

    def do_BaseModel(self, line):
        if line == ".all()":
            HBNBCommand().do_all("BaseModel")
        if line == ".count()":
            all_objs = storage.all()
            contar = 0
            for obj_id in all_objs.keys():
                if obj_id.split(".")[0] != "BaseModel":
                    continue
                contar += 1
            print(contar)
        if line[0:6] == ".show(" and line[-1] == ")":
            HBNBCommand().do_show("BaseModel " + line[7:-2])
        if line[0:9] == ".destroy(" and line[-1] == ")":
            HBNBCommand().do_destroy("BaseModel " + line[10:-2])
        if line[0:8] == ".update(" and line[-1] == ")":
            if line[-2] != "}":
                str1 = line[8:-1]
                str1 = "".join(str1.split(","))
                HBNBCommand().do_update("BaseModel " + str1)
            else:
                str1 = line[8:-1]
                str1 = str1.split(",")
                str2 = str1[0]
                del str1[0]
                dict1 = eval(",".join(str1))
                for i, j in dict1.items():
                    str3 = " \"" + i + "\" "
                    if type(j) is str:
                        str4 = "\"" + j + "\""
                        HBNBCommand().do_update("BaseModel " +
                                                str2 + str3 + str4)
                    else:
                        HBNBCommand().do_update("BaseModel " +
                                                str2 + str3 + str(j))


if __name__ == '__main__':
    """ should not be executed when imported """
    HBNBCommand.prompt = "(hbnb) "
    HBNBCommand().cmdloop()
