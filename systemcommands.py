from config import SYSTEM_COMMANDS, MODULES
from os import remove, path
import sys
from processing import process
from preprocessing import preprocess
import importlib.util

def add_system_command(command, func):
    SYSTEM_COMMANDS[command] = func

    
def safe_(command, blocks, preprocessed):
    """
    Takes the blocks and write them "As is" in the html
    """
    blocks = "\n".join([block.text for block in blocks])
    return .join(blocks)


def setup():
    """
    Adding all of the default system commands into the dictionary
    """
    add_system_command("^note", lambda x, y, z: None)
    add_system_command("@safe", safe_)
    add_system_command("@eval", eval_)
    add_system_command("@modules", modules_)
    add_system_command("@import", import_)