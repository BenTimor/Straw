from config import SYSTEM_COMMANDS
from systemcommands.eval_ import eval_
from systemcommands.import_ import import_
from systemcommands.loop_ import loop_
from systemcommands.safe_ import safe_

def add_system_command(command, func):
    SYSTEM_COMMANDS[command] = func

def setup():
    """
    Adding all of the default system commands into the dictionary
    """
    add_system_command("^note", lambda x, y, z: None)
    add_system_command("@safe", safe_)
    add_system_command("@eval", eval_)
    add_system_command("@import", import_)
    add_system_command("@loop", loop_)