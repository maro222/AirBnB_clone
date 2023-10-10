#!/usr/bin/python3

import json


import os


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
            for key in self.__objects.keys():
                dic[key] = self.__objects[key].to_dict()
            json.dump(dic, file)

    def reload(self):
        from models.base_model import BaseModel
        funcs = {"BaseModel": BaseModel}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                dic = json.load(file)
                for value in dic.values():
                    self.new(funcs[value['__class__']](**value))
