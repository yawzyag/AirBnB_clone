 # AirBnB_clone project!

![N|process](https://i.kym-cdn.com/photos/images/newsfeed/000/796/424/a75.jpg)
reference(https://www.quora.com/What-is-a-console-in-Python)


Basically , it is a CLI (command line interface ) which takes input in textual form and execute them . As , python ' s source is interpreted so in that console you just type a instructions and console execute it .

# Command line interpreter

firstly break the commands in words and take first word as program name and rest as command line arguments and execute them .

This is all you should at beginner level for more deeper information you should surfore about python console .


## Skeleton of the Interactive shell
The recommendation is to subclass the Cmd class, so that's what we do here, though as being a skeleton we don't do anything else with it.

    from cmd import Cmd
 
    class MyPrompt(Cmd):
        pass
 
    MyPrompt().cmdloop()

We create an instance object of the MyPrompt class and immediately call the cmdloop method. We could have used a temporary variable there if we wanted to be a bit more verbose like this:

    p = MyPrompt()
    p.cmdloop()
but the result is the same.

When we run this script it will display a default prompt:

    (Cmd)
    
You can't do much with it. You can type in ? and press ENTER to get the following help:

    Documented commands (type help <topic>):
    ========================================
    help

-----
