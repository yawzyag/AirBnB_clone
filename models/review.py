#!/usr/bin/python3
""" module to add the user into the project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Create review class """
    place_id = ""
    user_id = ""
    text = ""
