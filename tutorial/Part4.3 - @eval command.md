
# @eval - Nothing is impossible
@eval is a more difficult one, but it's the most important of all.

## @eval - Basic use
At the most basic layer, @eval allows you to run a Python code from your file and display the return value in your HTML file.

Note, you can also get information from the user via input().

**Example**  
Straw:

	span    
	    @eval
	    	inp = input("What's your name? ")
	    	if inp:
	    		return f"Hey {inp}!"
	    	else:
	    		return "Please enter your name"
Compiled HTML:
*- Compiler asks you 'What's your name?' in the command line*
*- You answer something, like 'Ben'*

    <span> Hey Ben! </span>


## @eval - Create a process command
Eval allows us to create process commands, just like @eval itself! (Fun fact, you can create an eval command in eval!) 
   
To do so, you have to give your module a name.
 **Note -** This type of commands is not going to run until you call them.

**Basic Example**
Straw:

    @eval(syscmd)
    	return "<span> Just testing </span>"
    
    @syscmd
Compiled HTML:

    <span> Just testing </span>
EZ-PZ. Lets face more advanced one.

**Advanced Command**
When you create a process command, you can use 2 new parameters. ***command*** and ***blocks***. We'll learn about these objects in the next part of the tutorial, but for now we just have to know two things:

***command.text*** returns us the text which is found after the process command.
***blocks[n].text*** returns us the content of the block. 

**Example**
Straw:

    @eval(printshit, 1)
	    arr = []
	    for block in blocks:
		    arr.append(block.text)
	    arr.insert(0, command.text)
	    return "\n".join(arr)
    
    @printshit SOME TEXT
	    1
	    2
	    3

Compiled HTML:

    SOME TEXT
    1
    2
    3
   
   We finished @eval! We finished EVIL!

**That's all for today.**



