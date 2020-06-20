from config import SYSTEM_COMMANDS
from systemcommands.eval_ import eval_
from systemcommands.import_ import import_
from systemcommands.loop_ import loop_
from systemcommands.safe_ import safe_
from systemcommands.set_ import set_
from systemcommands.compile_ import compile_
from systemcommands.terminal_ import terminal_
from systemcommands.tofile_ import tofile_
from systemcommands.delfile_ import delfile_
from systemcommands.readfile_ import readfile_

def add_system_command(command, func):
    SYSTEM_COMMANDS[command] = func

def setup():
    """
    Adding all of the default system commands into the dictionary
    """
    add_system_command("^note", lambda x, y, z: None)
    add_system_command("^set", set_)
    add_system_command("@safe", safe_)
    add_system_command("@eval", eval_)
    add_system_command("@import", import_)
    add_system_command("@loop", loop_)
    add_system_command("@compile", compile_)
    add_system_command("@terminal", terminal_)
    add_system_command("@tofile", tofile_)
    add_system_command("@delfile", delfile_)
    add_system_command("@readfile", readfile_)