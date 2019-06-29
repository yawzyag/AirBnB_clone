#!usr/bin/python3
""" module for create a base models """
import uuid
from datetime import datetime


class BaseModel:
    """ coments of class """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ testing str """
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dicty = self.__dict__.copy()
        dicty.update({'__class__': self.__class__.__name__})
        dicty['created_at'] = datetime.isoformat(dicty['created_at'])
        dicty['updated_at'] = datetime.isoformat(dicty['updated_at'])
        return dicty
