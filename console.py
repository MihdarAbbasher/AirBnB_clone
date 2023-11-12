#!/usr/bin/python3
""" module for interactive console """

import cmd


class HBNBCommand(cmd.Cmd):
    """interactive console cmd """

    prompt = "(hbnb) "

    def do_create_user(slef, line):
        """create new user"""
        print("create user")

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
