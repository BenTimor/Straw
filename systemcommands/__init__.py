from config import SYSTEM_COMMANDS
from glob import glob
from pathlib import Path
from systemcommands.eval_ import importfile #, eval_

ignore_files = ["__init__.py"]

def add_system_command(command, func):
    SYSTEM_COMMANDS[command] = func

def setup_files():
    """
    The past version of "setup" was too easy and I thought to myself
    'Ben, You really have to develop something a little more impressive'
    
    Everyone knows how much I like reflection in Java,
    So I've decided to use reflection in Python to import the system commands.
    
    And btw make it a little more prettier code.
    """
    path = Path(__file__).parent.absolute()
    files = glob(f"{path}/*.py")
    
    for file in files:
        name = file.replace(str(path) + "/", "", 1)
        if name in ignore_files:
            continue
        temp = importfile(name, file)
        add_system_command(temp.COMMAND, temp.run)
    
def setup():
    """
    Basically registers the system commands.
    """
    setup_files()
    # Another short commands
    add_system_command("^note", lambda x, y, z: None)
    add_system_command("@shortsafe", lambda command, blocks, preprocessed: command.text)