# The World Of Commands
In Straw, everything is a command (or a part of one). So it's important to know some.
## HTML Commands
As you already saw on part one of the tutorial, you can use HTML tags in Straw. And it's pretty easy!
Here's the structure of a HTML command.

    Tag(Parameters) Text
	    InnerTag(Another Parameters) Text
The only thing that you have to have in your code is the command itself (Tag). Anything else, like parameters and text is a suggestion.

### Example
Straw:

    head
	    title Hey
    body
	    p(style="color: red") Blah blah blah

Compiled to HTML:

    <!DOCTYPE html>
    <html> 
    <head> 
    <title> Hey
    </title>
    </head>
    <body> 
    <p style="color: red">  Blah blah blah
    </p>
    </body>
    </html>

## Preprocess Commands
In Straw we have two different types of system commands. The first type is 'Preprocess Command'.

Preprocess commands are mostly built-in, because there's no easy way to create them and they do one thing - running a Python code before the processing of the code.

Right now, Straw has only one preprocess command and it's ^note. This command just ignores anything which comes afterwards, so you can use it to note your file.

### Example:
    ^note(anotherhey) Hey
    	Hey2
    	Hey3
The straw compiler is just going to ignore all of this text.

The reason that we have this type of commands is because they can edit the preprocess objects and affect the processing.

## Process Commands
Similarly to preprocess commands, the process commands are here to run a Python code. The two big differences between them and the preprocess commands is that:
1. They are easy to write and everyone can add a new process command.
2. They return a code which is added to the html code.

In straw we have 4 built-in process commands, and you can use them anytime in any straw project.

### @safe | It's really safe here
@safe is the easiest to understand. It just returns anything its has inside.

**Example:**
Straw:

    @safe
    	<h1> Hey </h1>	
Compiled to HTML:

    <h1> Hey </h1>

### @eval | Basic use
@eval is a more difficult one, but it's required if you want to understand the another two commands.

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

### @eval | Creating Modules
if you want to create a module (A function like object of Straw, but without any parameters), you just have to name your code in the first parameters.

Note - Every parameters in Straw command is String. ALWAYS. So you don't have to use ""

**Example**
Straw:

    @eval(mymodule)
	    arr = []
	    for i in range(3):
		    arr.append(f"<span> {i} </span>")
	    return "\n".join(arr)
		    
		    

The module did nothing! But don't worry, the code worked. We don't have any output because we have to call our module (And I'll teach you how to do it very soon). **Modules don't run automatically!**

Until... You give them another two parameters. 0, and 1. So lets check out the next code:

    @eval(mymodule, 0, 1)
	    arr = []
	    for i in range(3):
		    arr.append(f"<span> {i} </span>")
	    return "\n".join(arr)
   
   Ok, so the last parameter - '1', tells @eval "I don't care that I just created a module, I want you to run it!".
   
   But the '0' tells it... Uhm... You'll see. Right now.
   

HTML Compiled:

    <span> 0 </span>
    <span> 1 </span>
    <span> 2 </span>

   
   
   ### @eval | Create a process command
   Eval allows us to create process commands, just like @safe and @eval themselfs! (Fun fact, you can create an eval command in eval!) 
   
   To do it, you have to give your module a name and move it the parameter '1'. Yes, in the last chapter when I told you to write this '0', I just told you to tell the compiler 'Dude, that's not a system command'. 
   **Note -** You cannot auto-run system commands via the third parameter.

**Basic Example**
Straw:

    @eval(syscmd, 1)
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
   
   ### @modules | Remeber the names of the evals?
   
   @modules simply allows you to call one or more modules (evals with a name which are not process commands).
   
   Lets call the module 'mymodule' which was created before.
   

    @modules(mymodule)
    ^note You also can call several modules! Like:
	    @modules(mymodule1, mymodule2)

Almost too easy.

### @import | When you want to put something in something else
import is really simple. It allows you to take another Straw file, and run it in your current file. And hear me out! It's not just putting the code of the file in your file, it also allows you to use its modules!

For example, let's assume we have a new file, which is called 'banana.sw' and it contains the following content:

    span banana.sw is imported here!
    @eval(bananamodule, 1)
	    return "BANANANANAA!!!"

And now in our file, we're importing this file:

    @import(banana.sw)
    span I put here something
    @bananamodule

The final HTML code, will look something like this:

    <span> banana.sw is imported here! </span>
    <span> I put here something </span>
    BANANANANAA!!!
**That's all for today.**
