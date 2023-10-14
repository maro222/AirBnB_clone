#!/usr/bin/python3

import json


class FileStorage:

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        objClassName = obj.__class__.__name__
        objId = obj.id
        self.__objects[f"{objClassName}.{objId}"] = obj

    def save(self):
        with open(self.__file_path, "w", encoding="utf-8") as file:
            dic = {}
            for key, value in self.__objects.items():
                dic[key] = value.to_dict()
            json.dump(dic, file)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        funcs = {"BaseModel": BaseModel, "User": User, "Place": Place,
                 "Amenity": Amenity, "City": City, "Review": Review,
                 "State": State}
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                dic = json.load(file)
                for value in dic.values():
                    self.new(funcs[value['__class__']](**value))
        except FileNotFoundError:
            pass
