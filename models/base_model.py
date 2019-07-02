#!usr/bin/python3
""" module for create a base models """
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ coments of class """

    def __init__(self, *args, **kwargs):
        """ init of basemodel """
        if kwargs:
            self.__updated_v(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __updated_v(self, kwargs):
        """ my function to update with kwargs """
        for key, val in kwargs.items():
            if key != "__class__":
                if key == "created_at" or key == "updated_at":
                    val = datetime.strptime(
                        kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, val)

    def __str__(self):
        """ testing str """
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ save changes """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """ return dict respresentation """
        dicty = self.__dict__.copy()
        dicty.update({'__class__': self.__class__.__name__})
        dicty['created_at'] = self.created_at.isoformat()
        dicty['updated_at'] = self.updated_at.isoformat()
        return dicty
