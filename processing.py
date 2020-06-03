from config import *
from preprocessing import Command, Block

def close_tags(processed, command, lastcommands):
    """
    Closes all of the tags (adding directly into the processed)
    """
    decrease = 0
    reversedcommands = lastcommands[::-1]
    
    # Reversing the lastcommands so the last one to open will be the first one to cloes
    for i in range(len(reversedcommands)):
        lastcommand = reversedcommands[i-decrease]
        if (not lastcommand.command.startswith("@") or lastcommand.command.startswith("^")) and command.spaces <= lastcommand.spaces:
            if lastcommand.command not in NOT_CLOSING_TAGS:
                processed.append(f"</{lastcommand.command}>")
            del reversedcommands[i-decrease]
            decrease += 1
        
    return reversedcommands[::-1]

def run_system_command(command, blocks, preprocessed):
    """
    Calls to the commands from the SYSTEM_COMMANDS dictionary
    """
    return SYSTEM_COMMANDS[command.command](command, blocks, preprocessed)
    
def process(preprocessed):
    """
    This function is processing the preprocessed content.
    It takes every object and turns it into HTML code.
    """
    processed = []
    lastcommands = []
    lastblocks = []
    
    # Runs preprocessed commands (^) 
    preprocessed.append(Command("^")) # Adds a command so it'll run one more time and close anything
    for command in preprocessed:
        if isinstance(command, Block):
            lastblocks.append(command)
            continue
        
        elif lastcommands and lastcommands[-1].command.startswith("^"):
            run_system_command(lastcommands[-1], lastblocks, preprocessed)  
            del lastcommands[-1]
            lastblocks = []

        if command.command.startswith("^"):
            lastcommands.append(command)
    
    lastblocks = []
    
    # Runs processed commands (@) and HTML tags
    preprocessed.append(Command("@")) # Adds a command so it'll run one more time and close anything
    for command in preprocessed:        
        if isinstance(command, Block):
            lastblocks.append(command)
            continue
        
        if lastcommands:
            if lastcommands[-1].command.startswith("@"):
                processed.append(run_system_command(lastcommands[-1], lastblocks, preprocessed))
                del lastcommands[-1]
                lastblocks = []
                
            if lastcommands[-1].command.startswith("^"):
                del lastcommands[-1]
                lastblocks = []
        
        lastcommands = close_tags(processed, command, lastcommands)
        lastcommands.append(command)
        
        if not (command.command.startswith("@") or command.command.startswith("^")):
            parms = " ".join(command.parms)
            parms = " " + parms if parms else ""
            processed.append(f"<{command.command}{parms}> {command.text}")
    
    # Returns the full html file without Nones
    return "\n".join([x for x in processed if x != None])