#!/usr/bin/python3
"""base model Moudle parent of all classes"""

from datetime import *
import uuid
from . import storage


class BaseModel:
    """BaseModel Class for all classes"""

    def __init__(self, *args, **kwargs):
        if len(kwargs.keys()) != 0:
            for key in kwargs.keys():
                if key == 'updated_at' or key == 'created_at':
                    self.__dict__[key] = datetime.fromisoformat(kwargs[key])
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save method to save in file"""

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self) -> dict:
        """to_dict method for return aft trans to ..."""

        dic = dict(self.__dict__)
        dic['__class__'] = self.__class__.__name__
        dic['updated_at'] = datetime.isoformat(dic.get('updated_at'))
        dic['created_at'] = datetime.isoformat(dic.get('created_at'))
        return dic
