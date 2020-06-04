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
        
class Block:
    """
    A block command object. Used  for preprocessing commands [^cmd] and processing commands [@cmd].
    Used to gain information which is indentationed after the command.
    For example:
    @Command Object
        Block Object
        Block Object 2
        Block Object 3
    """
    def __init__(self, text, spaces):
        self.text = text
        self.spaces = spaces

def count_spaces(line):
    """
    Counting the spaces at the start of a line
    """
    return len(line)-len(line.lstrip(' '))

def has_parameters(line):
    """
    Checks if the first word of the text has '(' attached to it.
    If it's attached, the command has parameters.
    """
    for char in list(line):
        if char == "(":
            return True
        if not (char.isalnum() or char == "@" or char == "^"):
            return False   
    return False

def find_command(line):
    """
    Finds the first word in the command, which is going to be used as the command itself.
    """
    return line.split("(" if has_parameters(line) else " ")[0]

def find_parameters(line):
    """
    Finding parameters of function.
    For example:
    ^cmd(parameter1, parameter2, parameter3) NOT A PARAMETER
        NOT A PARAMETER
    """
    if not has_parameters(line):
        return []
    return [arg.lstrip(" ") for arg in line.split(")", 1)[0].split("(")[1].split(",")]

def find_text(line):
    """
    Finding the text which comes after the command / the prameters of the command.
    ^cmd(NOT A TEXT) text text text
        NOT A TEXT
    """
    pattern = ")" if has_parameters(line) else " "
    if pattern in line:
        return line.split(pattern,1)[1]
    else:
        return ""

def preprocess(content, addhtml=True):
    """
    This function is preprocessing the content of a file.
    It takes everyline and converts it into a Command object / Block object.
    """
    # Just replacing the tabs with spaces and splitting the lines.
    lines = [" " + line for line in content.replace("\t", " ").split("\n")]
    if addhtml: lines.insert(0, "html")
    commands = []
    block = 0
    
    for line in lines:
        spaces = count_spaces(line)
        line = line.lstrip(" ")
        
        # If the line is empty, pass it
        if not line:
            continue
        
        # If the last command were a command which requires a block, it finds its block.
        if block:
            if spaces > block:
                commands.append(Block(line, spaces))
                continue
            else:
                # Resets the block
                block = 0
        
        # The only commands which require a block is Preproces commands (^) and Process commands (@)
        # So it sets the block to the amount of spaces of the command
        if line.startswith("@") or line.startswith("^"):
            block = spaces
        
        # It has to run for every command, it just adds it to the list of commands
        commands.append(Command(find_command(line), find_parameters(line), spaces, find_text(line)))
    return commands 