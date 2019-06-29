#!usr/bin/python3
""" module for create a base models """
import uuid


class BaseModel:
    """ coments of class """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def __str__(self):
        """ testing str """
        return ("[{}] ({}) {}/{} - {}/{}".
                format(self.__class__.__name__, self.id), seld.__dict__)

    def save(self):
        self.update_at = datetime.utcnow()

    def to_dict(self):
        return self.__dict__
        
