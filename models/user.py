#!/usr/bin/python3
""" module to add the user into the project """
from models.base_model import BaseModel


class User(BaseModel):
    """ Create user class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
