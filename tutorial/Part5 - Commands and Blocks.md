# Command and Blocks
This is going to be a really simple tutorial. It only requires you to know a little of Python.

Do you remember when I told you about command.text and blocks[n].text when you create a process command? Lets look around a little.

## Command - (Almost) Everything is a Command
The parameter 'command' that you get when you create a process command is a Command type.

The Command object is preprocessing object, which means it's created before the processing starts.

This is how it looks in the source code of Straw:

    class Command:
        """
        A command object, mainly for the preprocessing.
        Required for both HTML tags and system commands (both preprocessing commands [^cmd] and processing commands [@cmd])
        """
        def __init__(self, command="", parms=[], spaces=0, text=""):
            self.command = command
            self.parms = parms
            self.spaces = spaces
            self.text = text

### Lets Explain
Every Command object has 4 variables. 

**command -** The command itself. For example, if we're talking about @eval command, the command variable contains the string "@eval".
Don't forget that HTML tags are commands too. So if we're talking about `<b> </b>` tag, this variable contains the string "b".
**parms** - parms is an array which contains all of the parameters of the command. 
**text** - The text of the command. For example in the code `h1 hey`the text is "hey"
**spaces** - The spaces/tabs amount before the command.

## Block - If it's not a command, it's a Block

The only elements that have Blocks are the system commands (process and preprocess commands). It's just anything that is found in the block of the command.
**Note -** Any line is a new Block object.

Block is very similar to Command, but it has only two variables.

**text** - The block as a string (The original line itself).
**spaces** - The spaces/tabs amount before the block.

Now you're a pro Straw programmer. Soon you'll be able to learn how does the "reflection" work.
