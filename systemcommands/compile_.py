from subprocess import run, PIPE
from os import remove

def compile_(command, blocks, preprocessed):
    """
    Compiling a code of any language you want. 
    Syntax:
    @compile(file_to_compile, output_file, compile command, run command)
        CODE
    
    Example:
    @compile(file.c, a.out, gcc file.c, ./a.out)
    #include <stdio.h>
    int main() {
        printf("Hello, World!");
        return 0;
    }
    """
    if len(command.parms) >= 4:
        compilecommand = command.parms[2].split(" ")
        runcommand = command.parms[3].split(" ")
        filename = command.parms[0]
        outputfile = command.parms[1]
        
        with open(filename, "w") as file:
            file.write("\n".join([block.text for block in blocks]))
        
        run(compilecommand, stdout=PIPE)
        result = run(runcommand, stdout=PIPE)
        
        remove(filename)
        remove(outputfile)
        
        return result.stdout.decode()