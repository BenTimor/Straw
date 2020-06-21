from subprocess import run, PIPE

COMMAND = "@terminal"

def run(command, blocks, preprocessed):
    outputs = []
    for block in blocks:
        result = run(["sh", "-c", block.text], stdout=PIPE)
        outputs.append(result.stdout.decode())
    
    if command.parms and command.parms[0] == "0":
        return None
    
    return "\n".join(outputs)