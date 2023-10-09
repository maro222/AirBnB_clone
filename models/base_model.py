#!/usr/bin/python3

from datetime import *
import uuid


class BaseModel:
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

    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dic = self.__dict__
        dic['__class__'] = __class__.__name__
        dic['updated_at'] = datetime.isoformat(dic.get('updated_at'))
        dic['created_at'] = datetime.isoformat(dic.get('created_at'))
        return dic
