#!/usr/bin/python3
import cmd
"""
This is a module where you define your class HBNBCommand
and it is where implements commands for creating, showing, destroying, updating and listing
instances of classes that inherit from BaseModel.

Inside the console there is a prompt before a user enters a command that is hbnb and a user enters in this format (hbnb) command class_name class_id [attribute_name] [attribute_value]
"""
class HBNBCommand(cmd.Cmd):
"""
