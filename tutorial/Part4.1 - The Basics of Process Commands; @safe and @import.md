
# Process Commands
Similarly to preprocess commands, the process commands are here to run a Python code. The two big differences between them and the preprocess commands are:
1. They are easy to write and everyone can add a new process command.
2. They return a code which is added to the HTML file.

We're going in the next chapters to learn about some process commands.

## @safe | It's really safe here
@safe is the easiest to understand. It just returns anything its has inside. And sometimes adds a HTML tag.

### Basic Example:
Straw:

    @safe
    	<h1> Hey </h1>	
Compiled to HTML:

    <h1> Hey </h1>

### More Advanced One
Sometimes you want the engine not to compile something between two tags. @safe comes to do it easily, by adding the tag to the text of the command. Lets look at an example:

Straw:

    @safe style
	    h1 {
	    color: red;
	    }
HTML output:

    <style>
    h1 {
    color: red;
    }
    </style>

## @import - When you want to merge files
You may actually know @import from another programming languages. Straw is very similar to them.
This command is doing a simple thing, It copies anything from a file, compiles it and puts it in the code.

It can get more than one file.

### Example
Lets assume we have two different files. The one is index.sw and the other is style.sw. 
**The content of style.sw:**

    @safe style
      h1 {
        color: red;
      }

**The content of index.sw:**

    head
      @import(style.sw)
    
    body
      h1 Hey
      
If you followed me, You can guess that the output is going to be a red "Hey" title. The HTML output:

    <html>
    <head>
    <style>
    h1 {
      color: red;
    }
    </style>
    </head>
    <body>
    <h1> Hey </h1>
    </body>
    </html>


