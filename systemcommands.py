from config import SYSTEM_COMMANDS, MODULES
from os import remove, path
import sys
from processing import process
from preprocessing import preprocess
import importlib.util

def add_system_command(command, func):
    SYSTEM_COMMANDS[command] = func

def importfile(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo
    
def safe_(command, blocks, preprocessed):
    """
    Takes the blocks and write them "As is" in the html
    """
    blocks = [block.text for block in blocks]
    return "\n".join(blocks)

def eval_(command, blocks, preprocessed):
    """
    Takes a python code and puts the return in the HTML
    """
    if blocks:
        first_spaces = blocks[0].spaces
        spaces_amount = 0
        
        # Check how many spaces any block has, and uses it to insert everything into a function
        # And ofc adds the spaces to the start of everyblock because preprocessing removes the spaces
        for block in blocks:
            block.spaces = block.spaces-first_spaces
            
            if not block.spaces and not spaces_amount:
                spaces_amount = block.spaces
                
        spaces_amount = spaces_amount if spaces_amount else 2
        
        blocks = [" "*(spaces_amount+block.spaces) + block.text for block in blocks]
        blocks.insert(0, "def run(command=None, blocks=None, preprocessed=None):")
        blocks = "\n".join(blocks)
                
        temp = None
        
        if not command.parms:
            rpath = ""
            with open("temp.py", "w") as file:
                file.write(blocks)
                rpath = path.realpath(file.name)
                
            # Import the module
            temp = importfile("temp", rpath)
            # Running it and "destroying" the var
            temp = temp.run()
            # Unloading the module in a stupid way. BUT in this case, I think it's the best way to do it
            # del sys.modules["temp"]
            remove("temp.py")
            
        else:
            name = command.parms[0]
            syscmd = command.parms[1] if len(command.parms) > 1 else "0"
            
            if syscmd == "0":
                # If you don't want it to be a system command
                # Check if you want to run it 
                run = command.parms[2] if len(command.parms) > 2 else "0"
                run = False if run == "0" else True

                rpath = ""
                with open(f"{name}.py", "w") as file:
                    file.write(blocks)
                    rpath = path.realpath(file.name)

                # It's really like the if before, But here we won't unload the module and safe it for a future use
                MODULES[name] = importfile(name, rpath)
                if run: temp = MODULES[name].run()
                remove(f"{name}.py")
            
            else:
                rpath = ""
                with open(f"{name}.py", "w") as file:
                    file.write(blocks)
                    rpath = path.realpath(file.name)
                    
                # Add it to sys commands
                mod = importfile(name, rpath)
                add_system_command(f"@{name}", mod.run)
                remove(f"{name}.py")
        
        return temp

def modules_(command, blocks, preprocessed):
    """
    Calling a module (or a list of modules) which created by the @eval command
    """
    temp = []
    for parm in command.parms:
        try:
            temp.append(MODULES[parm].run())
        except KeyError as e:
            temp.append("The module " + parm + " doesn't exist.")
    return "\n".join(temp) if temp else None

def import_(command, blocks, preprocessed):
    temp = []
    for parm in command.parms:
        with open(parm, "r") as file:
            html = process(preprocess(file.read(), False))
            temp.append(html)
    
    temp = [x for x in temp if x]
    return "\n".join(temp) if temp else None    

def setup():
    """
    Adding all of the default system commands into the dictionary
    """
    add_system_command("^note", lambda x, y, z: None)
    add_system_command("@safe", safe_)
    add_system_command("@eval", eval_)
    add_system_command("@modules", modules_)
    add_system_command("@import", import_)