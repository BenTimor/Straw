
# Preprocess Commands
In Straw we have two different types of system commands. The first type is 'Preprocess Command'.

Preprocess commands are mostly built-in, because there's no easy way to create them. These command are programmed to do only one thing - running a Python code before of the processing of the code.

The advantage of this commands is the fact that they can edit the preprocessing information before the process itself.

We're going to learn about two different preprocess commands.

## ^note - I need to write it down
^note command is used similarly to '#' in Python. you use it to note things for yourself. Anything that comes after/inside a ^note command will not be processed by the engine.
### For example:

    ^note(anotherhey) Hey
    	Hey2
    	Hey3
The straw engine is just going to ignore all of this text.

## ^set - Like variables, But not.
Sometimes you use the same information again and again. Because we want it to be easier to makes changes, we don't want to hard-code this information.

So Straw gives you the optimal solution - Tell the engine what to you want to replace in your code. That's very similar to variables, but a little bit different. Let's see.

### This is the structure of ^set command

    ^set(oldtext) newtext
Easy.

### Example
Straw code:

    ^set(hello) Hello World!
    span hello

HTML code:

    <span> Hello World! </span>

As you can see, the word "hello" was replaced by "Hello World!".

**Note:** This command is replacing  a text of your choice in any text of any HTML command. It won't replace anything in preprocess and process command, won't replace anything in blocks and won't replace anything in the parameters.

We very recommend to everyone to set a special char before/after the word he wants to replace so he won't replace anything important. For example:

    ^set({hello}) Hello World!
This will replace any "{hello}" with "Hello World!"
 
**Lets continue and learn about process commands!**
