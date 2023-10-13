#!/usr/bin/python3

import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    list_of_classes = ["BaseModel", "User", "State", "City", "Amenity",
                       "Place", "Amenity", "Review"]

    def do_EOF(self, line):
        """EOF is to exit else"""
        print()
        return True

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        """emptyline pass"""
        pass

    def do_help(self, line):
        """help to show all commanda"""
        return super().do_help(line)

    def do_create(self, line):
        if len(line) == 0:
            print("** class name missing **")
        elif len(line) > 0 and line not in HBNBCommand.list_of_classes:
            print("** class doesn't exist **")
        else:
            ins = eval(line)()
            ins.save()
            print(ins.id)

    def do_show(self, line):
        arr = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif len(arr) == 1:
            if (arr[0] not in HBNBCommand.list_of_classes):
                print("** class doesn't exist **")
            print("** instance id missing **")
        elif (len(arr) == 2):
            if (arr[0] not in HBNBCommand.list_of_classes):
                print("** class doesn't exist **")
            for key, value in FileStorage().all().items():
                if f"{arr[0]}.{arr[1]}" == key:
                    print(value)
                    break
            print("** no instance found **")

    def do_destory(self, line):
        arr = line.split()
        if (len(arr) == 0):
            print("** class name missing **")
        elif (len(arr) == 1):
            if (arr[0] not in HBNBCommand.list_of_classes):
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            for key, value in FileStorage().all().items():
                isFound = False
                if (f"{arr[0]}.{arr[1]}" == key):
                    del storage.all()[key]
                    storage.save()
                    isFound = True
                    break
            if (isFound is False):
                print("** no instance found **")

    def do_all(self, line):
        arr = line.split()
        emptyArr = []
        for key, value in FileStorage().all().items():
            emptyArr.append(str(value))
        if (len(arr) == 0):
            print(emptyArr)
        elif (len(arr) == 1):
            if (arr[0] in HBNBCommand.list_of_classes):
                print(emptyArr)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        arr = line.split()
        if (len(arr) == 0):
            print("** class name missing **")
        elif (len(arr) == 1):
            if (arr[0] not in HBNBCommand.list_of_classes):
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif (len(arr) == 2):
            print("** attribute name missing **")
        elif (len(arr) == 3):
            print("** value missing **")
        else:
            if arr[3][0] == '"':
                value_edit = arr[3][1:-1]
            elif arr[3].isdigit():
                value_edit = int(arr[3])
            else:
                value_edit = arr[3]
                for key, value in FileStorage().all().items():
                    if (f"{arr[0]}.{arr[1]}" == key):
                        setattr(value, arr[2], value_edit)
                        FileStorage().save()
                        break

    def do_count(self, line):
        if line == "" or not line:
            print("** class name missing **")
        else:
            arg = line.split('.')
            if arg[0] not in list_of_classes:
                print("** class dosenot exist")
            else:
                count = 0
                for key in storage.all().keys():
                    key = key.split('.')
                    if key == arg:
                        cout += 1
                print(count)

    def default(self, line):
        emptyArr = []
        i = 0
        if '.' in line:
            arr_of_line = line.split(".")
            if (arr_of_line[0] in HBNBCommand.list_of_classes):
                if (arr_of_line[1] == "all()"):
                    for key, value in FileStorage().all().items():
                        helper = key.split(".")
                        original_class = helper[0]
                        if (arr_of_line[0] == original_class):
                            emptyArr.append(str(value))
                    print(emptyArr)
                elif (arr_of_line[1] == "count()"):
                    for key, value in FileStorage().all().items():
                        helper = key.split(".")
                        original_class = helper[0]
                        if (arr_of_line[0] == original_class):
                            i += 1
                    print(i)
                elif (arr_of_line[1][0:4] == "show"):
                    is_found = False
                    spec_id = arr_of_line[1][6:-2]
                    for key, value in FileStorage().all().items():
                        helper = key.split(".")
                        original_class = helper[0]
                        if (arr_of_line[0] == original_class):
                            if (getattr(value, "id") == spec_id):
                                emptyArr.append(str(value))
                                print(emptyArr)
                                is_found = True
                    if is_found is False:
                        print("** no instance found **")
                elif (arr_of_line[1][0:7] == "destory"):
                    is_found = False
                    spec_id = arr_of_line[1][9:-2]
                    for key, value in FileStorage().all().items():
                        helper = key.split(".")
                        original_class = helper[0]
                        if (arr_of_line[0] == original_class):
                            if (getattr(value, "id") == spec_id):
                                del storage.all()[key]
                                storage.save()
                                is_found = True
                                break
                    if (is_found is False):
                        print("** no instance found **")
                elif (arr_of_line[1][0:6] == "update" and arr_of_line[1][-2] == "}"):
                    is_found = False
                    anoth_arr = arr_of_line[1].split(",", 1)
                    spec_id = anoth_arr[0][8:-1]
                    dic_for_update = eval(anoth_arr[1][1:-1])
                    for key, value in FileStorage().all().items():
                        helper = key.split(".")
                        original_class = helper[0]
                        if (arr_of_line[0] == original_class):
                            if (getattr(value, "id") == spec_id):
                                is_found = True
                                for k, v in dic_for_update.items():
                                    setattr(value, k, v)
                                storage.save()
                                break
                    if is_found is False:
                        print("** no instance found **")
                elif (arr_of_line[1][0:6] == "update" and arr_of_line[1][-2] != "}"):
                    is_found = False
                    anoth_arr = arr_of_line[1].split(",", 2)
                    spec_id = anoth_arr[0][8:-1]
                    k = anoth_arr[1][2:-1]
                    v = anoth_arr[2][1:-1]
                    for key, value in FileStorage().all().items():
                        helper = key.split(".")
                        original_class = helper[0]
                        if (arr_of_line[0] == original_class):
                            if (getattr(value, "id") == spec_id):
                                is_found = True
                                if (v[0] == '"'):
                                    v = v[1:-1]
                                elif (v.isdigit()):
                                    v = int(v)
                                setattr(value, k, v)
                                storage.save()
                                break
                    if is_found is False:
                        print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
