#!usr/bin/python3
""" module for create a base models """


class FileStorage:
    __file_path = ""
    __objects = {}

    def all(self):
        __objects = "{}.{}".format(self.__class__.__name__, self.id)
