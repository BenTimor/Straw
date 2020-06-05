from systemcommands.eval_ import eval_
from systemcommands.import_ import import_
from config import SYSTEM_COMMANDS

def add_system_command(command, func):
    SYSTEM_COMMANDS[command] = func

def setup():
    """
    Adding all of the default system commands into the dictionary
    """
    add_system_command("^note", lambda x, y, z: None)
    add_system_command("@safe", lambda _, blocks, __: "\n".join([block.text for block in blocks]))
    add_system_command("@eval", eval_)
    add_system_command("@import", import_)