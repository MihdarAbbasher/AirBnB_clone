#!/usr/bin/python3
""" module for interactive console """

import cmd


class My_cmd(cmd.Cmd):
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


if __name__ == '__main__':
    My_cmd().cmdloop()
