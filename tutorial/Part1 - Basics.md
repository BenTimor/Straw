# Basic Tutorial
In this tutorial we're going to learn about the basics of Straw.

## Required Knowledge
1. HTML basics
2. Some programming background. **Recommended** - Python basics
3. A brain can help sometimes.

## What is a (basic) command in Straw
It might seem unnecessary to know, but it's really important to understand what is a Straw command. 
For starters, everything in straw is a command or a part of one.

So what does a command look like? Here's a simple example, the explanation is right after the code.

    span(id=p1, style="color: red") Hello World!
Every command must start with the command itself. In this case, the command is 'span', because it's the first word in the sentence.  So if you just want to run the command, you can write:

    span

Sometimes you'd **like** to give the command some parameters. Mostly, you don't **have** to do it. 
If you have a basic understanding of programming languages, you're gonna to notice that our parameters are 'id=p1' and 'style="color: red"'.

If it's not clear, you specify parameters between '(' and ')', and you're splitting them via ','.
Also, an important law which is not right for most programming languages, in Straw you have to attach the parameters to the command, you can't put space between them. For example:

**The right way:**

    span(parameters)

**The wrong way**

    span (parameters)

When you want to specify more than one parameter, you put ',' between your parameters. If you want to use comma as part of one of the parameters, you have to use double-comma `',,'` 

The last part of our command is a text which comes right after the command, some commands uses this text to do things. 
As you may already understand, our text is 'Hello World!'. 
Now, lets understand an advanced command.

## What is an advanced (system) command in Straw
I'm not going to explain what these commands do and why they're different from basic commands, but I am going to show you how they look like, so you'll be able to understand them soon.

This is two examples of 'advanced' commands. We're calling these types of commands 'system commands' in Straw.

    ^note Hey!
	    I'd like to note it.

    @safe
	    <b> I'm so bold </b>
	    <p> I'm not :( </p>
These command are very similar to the basic ones, they also can get parameters and additional text. But they got two differences.
1. They start with '^' or '@'. 
2. They have blocks. If you indenting via spaces/tabs the next line/s, it becomes part of the command.

Now, we're after the basic. It was the hard part I swear. 
