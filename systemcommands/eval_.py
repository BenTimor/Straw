import systemcommands
import importlib.util
from os import remove, path

def importfile(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo

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
                
            # Import the module and then removing it
            temp = importfile("temp", rpath)
            remove("temp.py")
            return temp.run()
            
        else:
            name = command.parms[0]
            
            rpath = ""
            with open(f"{name}.py", "w") as file:
                file.write(blocks)
                rpath = path.realpath(file.name)
                    
            # Add it to sys commands
            mod = importfile(name, rpath)
            systemcommands.add_system_command(f"@{name}", mod.run)
            remove(f"{name}.py")
        
        return temp
