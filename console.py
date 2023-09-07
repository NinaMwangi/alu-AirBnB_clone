#!/usr/bin/python3
"""This module is the entry point for the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Hbnb Command Processor"""

    prompt = '(hbnb)'

    def do_EOF(self, arg):
        """EOF command to exit the program \n"""
        return True
    
    def do_quit(self, arg):
        """Quit command to exit the program \n"""
        return True
    
    def do_help(self, arg: str):
        """Describes what the methods do"""
        return super().do_help(arg)
    
    def emptyline(self):
        """Empty line + Enter doesnt execute"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()