#!usr/bin/python3
""" module for create a base models """
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ coments of class """

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.__updated_v(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __updated_v(self, kwargs):
        for key, val in kwargs.items():
            if key is not "__class__":
                if key is "created_at":
                    time = datetime.strptime(
                        kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, time)
                elif key is "updated_at":
                    time = datetime.strptime(
                        kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, time)
                else:
                    setattr(self, key, val)

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
