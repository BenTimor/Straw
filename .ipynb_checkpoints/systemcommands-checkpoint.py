from config import SYSTEM_COMMANDS

def compile_(command, blocks, preprocessed):
    pass # TBC

def safe_(command, blocks, preprocessed):
    blocks = [block.text for block in blocks]
    return "\n".join(blocks)

def add_system_command(command, func):
    SYSTEM_COMMANDS[command] = func

def setup():
    """
    Adding all of the default system commands into the dictionary
    """
    add_system_command("^note", lambda x, y, z: None)
    add_system_command("@safe", safe_)
    add_system_command("@compile", compile_)