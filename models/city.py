#!/usr/bin/python3
"""Module to get the BaseModel."""


from models.base_model import BaseModel


class City(BaseModel):
    """Class City inh...erited from his father.... BaseModel."""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
