#!usr/bin/python3
""" module for create a file serialization-deserialization """
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ class for manage storage """
    __file_path = "file.json"
    __objects = {}

    dic = {"BaseModel": BaseModel, "User": User,
           "Place": Place, "State": State,
           "Amenity": Amenity, "Review": Review, "City": City}

    def all(self):
        """ returns the dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects """
        new_obj = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[new_obj] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        listm = {}
        for key, val in FileStorage.__objects.items():
            listm.update({key: val.to_dict()})
        filename = FileStorage.__file_path
        with open(filename, "w") as write_file:
            write_file.write(json.dumps(listm))

    def reload(self):
        """ deserializes the JSON file to __objects """
        filename = FileStorage.__file_path
        FileStorage.__objects = {}
        try:
            with open(filename) as fileo:
                objecs = json.load(fileo)
            for key, val in objecs.items():
                cl = val["__class__"]
                FileStorage.__objects[key] = FileStorage.dic[cl](**val)
        except:
            pass
