from processing import process
from preprocessing import preprocess

def loop_(command, blocks, preprocessed):
    if command.parms:
        times = 0
        try:
            times = int(command.parms[0])
        except:
            return None
        
        var = command.parms[1] if len(command.parms) > 1 else None
        blocks = "\n".join([" "*block.spaces + block.text for block in blocks])
        total = []
                
        for i in range(times):
            copy_blocks = blocks.replace(var, str(i+1)) if var else blocks
            total.append(process(preprocess(copy_blocks, False)))
        
        return "\n".join(total)