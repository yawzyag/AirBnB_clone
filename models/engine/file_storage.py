#!usr/bin/python3
""" module for create a file serialization-deserialization """
import json
from models.base_model import BaseModel


class FileStorage:
    """ class for manage storage """
    __file_path = "file.json"
    __objects = {}

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
        ''' deserializes the JSON file to __objects '''
        filename = FileStorage.__file_path
        FileStorage.__objects = {}
        try:
            with open(filename) as fileo:
                objecs = json.loads(fileo.read())
            for key, val in objecs.items():
                for i, j in val.items():
                    objecs.update({key : BaseModel({i : j})})
            FileStorage.__objects = objecs
        except:
            pass
