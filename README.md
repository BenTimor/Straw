﻿# Straw - A WIP Client-Side Programming Language

[Fork project in Rust programming language](https://github.com/BenTimor/IronStraw)

> There's nobody who doesn't know about HTML. The 'must have' client-side programming language for every website. You literally have to build your website template via HTML tags, because it's the only language browser support.
> 
> I say, no more! We have to walk into the future. We have to develop new features, new languages and new frameworks which is coming to replace the HTML language.

Straw is a new programming language and it lets you create easily web files. So why using Straw instead of HTML?

 1. First of all, the code of straw is a lot more elegant than HTML code. And the more **beautiful** the code is, the **easier** to work about the website.
 2. Straw contains a lot of features which **doesn't exist** in pure HTML. those features let you dynamically generate new web files. For example, you can write new functions and import files of **another programming languages** into your Straw code!
 3. For the general purpose, Straw may be **easier**, and the code may be **shorter**. You don't have to close tags and you can see which tag is found inside another.
 
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

