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

But what if you want to use multi-line tag? You'll have to use @safe command, which we'll learn very soon.

