def tofile_(command, blocks, preprocessed):
    if command.parms:
        with open(command.parms[0], "w") as file:
            spaces = None
            for block in blocks:
                if spaces == None: spaces = block.spaces
                file.write(" "*(block.spaces-spaces) + block.text + "\n")