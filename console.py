#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
