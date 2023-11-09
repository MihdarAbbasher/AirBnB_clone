import cmd
""" module for interactive console """

class My_cmd(cmd.Cmd):
    """interactive console cmd """
    def do_create_user(slef, line):
        print ("create user")

    def do_EOF(self, line):
        """exit from sonsole"""
        return True

if __name__ == '__main__':
    My_cmd().cmdloop()
