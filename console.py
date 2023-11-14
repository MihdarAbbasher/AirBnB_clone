#!/usr/bin/python3
""" module for interactive console """

import cmd
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """interactive console cmd """

    prompt = "(hbnb) "
    myInstances = {"BaseModel": BaseModel, "User": User}

    def do_create(slef, line):
        """create new instance"""
        if not line:
            print("** class name missing **")
            return
        myClass = line.split(" ")[0]
        if myClass not in HBNBCommand.myInstances:
            print("** class doesn't exist **")
            return
        print(myClass)
        newIns = HBNBCommand.myInstances[myClass]()
        print("class: {}, id: {}".format(myClass, newIns.id))

    def do_EOF(self, line):
        """exit from sonsole"""
        return True

    def do_help(self, line):
        """show general or specific help"""
        print()
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit\n")

    def do_quit(self, line):
        """ exit from console"""
        return True

    def emptyline(self):
        """Override defaults of`empty line & return`.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
