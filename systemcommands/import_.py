from processing import process
from preprocessing import preprocess

COMMAND = "@import"

def run(command, blocks, preprocessed):
    temp = []
    for parm in command.parms:
        with open(parm, "r") as file:
            html = process(preprocess(file.read(), False))
            temp.append(html)
    
    temp = [x for x in temp if x]
    return "\n".join(temp) if temp else None    
