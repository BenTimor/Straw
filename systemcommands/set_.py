from preprocessing import Command

COMMAND = "^set"

def run(command, blocks, preprocessed):
    if command.parms:
        var = command.parms[0]
        to = command.text
        
        for obj in preprocessed:            
            if isinstance(obj, Command) and not (obj.command.startswith("@") or obj.command.startswith("^")):
                obj.text = obj.text.replace(var, to)