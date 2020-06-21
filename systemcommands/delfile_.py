from os import remove

COMMAND = "@delfile"

def run(command, blocks, preprocessed):
    if command.parms:
        remove(command.parms[0])