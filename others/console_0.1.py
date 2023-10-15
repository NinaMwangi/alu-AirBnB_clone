#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd
from file_storage import FileStorage
from BaseModel2 import BaseModel

storage = FileStorage()


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    instance_id = args[1]
                    key = "{}.{}".format(class_name, instance_id)
                    if key in storage.all():
                        print(storage.all()[key])
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    instance_id = args[1]
                    key = "{}.{}".format(class_name, instance_id)
                    if key in storage.all():
                        del storage.all()[key]
                        storage.save()
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        if not args:
            obj_list = []
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
        else:
            try:
                class_name = args[0]
                if class_name in BaseModel.__subclasses__():
                    obj_list = []
                    for key, obj in storage.all().items():
                        if class_name in key:
                            obj_list.append(str(obj))
                    print(obj_list)
                else:
                    print("** class doesn't exist **")
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                if class_name in BaseModel.__subclasses__():
                    if len(args) < 2:
                        print("** instance id missing **")
                    else:
                        instance_id = args[1]
                        key = "{}.{}".format(class_name, instance_id)
                        if key in storage.all():
                            if len(args) < 3:
                                print("** attribute name missing **")
                            else:
                                attribute_name = args[2]
                                if len(args) < 4:
                                    print("** value missing **")
                                else:
                                    attribute_value = args[3]
                                    instance = storage.all()[key]
                                    setattr(instance, attribute_name,
                                            attribute_value)
                                    instance.save()
                        else:
                            print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            except NameError:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
