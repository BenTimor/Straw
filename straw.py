from processing import process
from preprocessing import preprocess
from systemcommands import setup
from sys import argv as args

def main():
    del args[0]
    if not args:
        print("You have to specify the file/s")
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
            
            print(f"The file {arg} compiled.")
                
        except FileNotFoundError as e:
            print(f"Hey! One of the files ({arg}) doesn't exist. Continuing with all of the other files...")
        
#         except ModuleNotFoundError as e:
#             print("Hey! One of the modules in this file is not found. Sometimes it's happing due to an error and running again will solve the problem.")
#             print("If running the compiling again didn't solve it, You may have missing files in your folder.")
            
if __name__ == "__main__":
    main()