#!/usr/bin/python3
""" module to create the console """
import cmd


class HBNBCommand(cmd.Cmd):
    "Command processor for HBNB\n"

    def emptyline(self):
        return

    def do_EOF(self, line):
        "Exit\n"
        return True

    def do_quit(self, line):
        "Quit command to exit the program\n"
        return True


if __name__ == '__main__':
    HBNBCommand.prompt = "(hbnb) "
    HBNBCommand().cmdloop()
