#!/usr/bin/python3
""" module for interactive console """

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """interactive console cmd """

    prompt = "(hbnb) "
    myInstances = {"BaseModel": BaseModel, "User": User, "City": City, "State": State, "Place": Place, "Review": Review,
    "Amenity": Amenity}

    def do_create(slef, line):
        """create new instance"""
        if not line:
            print("** class name missing **")
            return
        myClass = line.split(" ")[0]
        if myClass not in HBNBCommand.myInstances:
            print("** class doesn't exist **")
            return
        newIns = HBNBCommand.myInstances[myClass]()
        print(newIns.id)

    def do_EOF(self, line):
        """exit from sonsole"""
        return True

    def do_show(self, line):
        """exit from sonsole"""
        if not line:
            print("** class name missing **")
            return
        myline = line.split(" ")
        if myline[0] not in HBNBCommand.myInstances:
            print("** class doesn't exist **")
            return
        if len(myline) < 2:
            print("** instance id missing **")
            return
        items = storage.all()
        key = myline[0] + "." + myline[1]
        for k in items:
            if key == k:
                print(items[k])
                return
        print("** no instance found **")

    def do_destroy(self, line):
        """delete instance and save"""
        if not line:
            print("** class name missing **")
            return
        myline = line.split(" ")
        if myline[0] not in HBNBCommand.myInstances:
            print("** class doesn't exist **")
            return
        if len(myline) < 2:
            print("** instance id missing **")
            return
        items = storage.all()
        key = myline[0] + "." + myline[1]
        for k in items:
            if key == k:
                del (items[k])
                storage.save()
                return
        print("** no instance found **")

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

    def do_all(self, line):
        """show all instances"""
        items = storage.all()
        if not line:
            for k in items:
                print(items[k])
            return
        myline = line.split(" ")
        if myline[0] not in HBNBCommand.myInstances:
            print("** class doesn't exist **")
            return
        for k in items:
            if isinstance(items[k], HBNBCommand.myInstances[myline[0]]):
                print(items[k])



if __name__ == '__main__':
    HBNBCommand().cmdloop()
