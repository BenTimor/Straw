from os import remove

def delfile_(command, blocks, preprocessed):
    if command.parms:
        remove(command.parms[0])