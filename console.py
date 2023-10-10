#!/usr/bin/python3

import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    list_of_classes = ["BaseModel"]
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
            if (isFound == False):
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
            if arr[3].isdigit():
                value_edit = int(arr[3])
            elif arr[3][-1] == '"' and arr[3][0] == '"':
                value_edit = arr[3][1:-1]
            else:
                value_edit = arr[3]
                for key, value in FileStorage().all().items():
                    if (f"{arr[0]}.{arr[1]}" == key):
                        setattr(value, arr[2], value_edit)
                        FileStorage().save()
                        break


if __name__ == '__main__':
    HBNBCommand().cmdloop()
