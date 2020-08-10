# Straw - a Template Engine Structure
Straw is a Python project which is created so I'll be able to develop it again in another programming languages.
I'm developing this project again and again in another languages because it's simple enough to develop when I'm new to the language, but advanced enough so I'll be able to learn something.

[More information for Hebrew speakers on my blog.](https://bentimor.com/straw/)

[Fork project in Rust programming language](https://github.com/BenTimor/IronStraw)
 
Currently, this project is totally abandoned and I'm not working on it, I just use it as a structure.

## Requirements
 - Python 3.x

## Installation and Usage
We're on pip!
You can install Straw easily via the following command:

    pip install StrawEngine
Now, if you want to 'compile' a file, you can do it via the following command:

    straw file(,file2,file3...)

## Tutorial
You can read the tutorial in the [tutorial](https://github.com/BenTimor/Straw/tree/master/tutorial) folder.

## Code Example
Straw code:

    head
      title This is my website!
    
    body
      center
        h1 Hello! :)
        p Welcome to my website. Love you.
          ^note I'm adding the safe so it won't close the p tag.
          @safe
            I have nothing to say anymore.
    
      ^note It's a stupid idea but I like it
      @eval
        return "Credit - Ben Timor, https://bentimor.com"

Compiling into the HTML code:

    <!DOCTYPE html>
    <html> 
    <head> 
    <title> This is my website!
    </title>
    </head>
    <body> 
    <center> 
    <h1> Hello! :)
    </h1>
    <p> Welcome to my website. Love you.
    I have nothing to say anymore.
    </p>
    </center>
    Credit - Ben Timor, https://bentimor.com
    </body>
    </html>

