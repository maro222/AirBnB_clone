#!/usr/bin/python3
"""Module to take from the BaseModel."""
from models.base_model import BaseModel


class User(BaseModel):
    """Class User inheri...ted fr...om BaseModel."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
