from processing import process
from preprocessing import preprocess
from systemcommands import setup
from sys import argv
from os import path
from logging import warning

def main(args, cmd=False):
    if cmd: del args[0]
    if not args:
        if cmd: print("You have to specify the file/s")
        return
    
    setup()
    
    for arg in args:
        try:
            html = ""
            with open(arg, "r") as file:
                html = process(preprocess(file.read()))
            
            filename = arg.split(".")[0]
            with open(f"{filename}.html", "w") as file:
                file.write("<!DOCTYPE html>\n" + html)
            
            if cmd: print(f"The file {arg} compiled.")
                
        except FileNotFoundError as e:
            if cmd: print(f"Hey! One of the files ({arg}) doesn't exist. Continuing with all of the other files...")
            else: warning(f"One of the files ({arg}) is not found. ")
            
if __name__ == "__main__":
    main(argv, True)
