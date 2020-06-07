# @loop and @compile
## @loop - Again and again and again...
@loop allows you to run a Straw code multiple times and even using information variables. The are two types of loops.
The first one is **range loop**.

With range loop, You just give the loop a number and it'll run the code inside this number of times. If you specify another parameter, It'll be used as the index of the loop.

### Range Loop Example

    @loop(3)
      span Hey
    
    @loop(2, i)
      span i
Output:

    <span> Hey </span>
    <span> Hey </span>
    <span> Hey </span>
    <span> 1 </span>
    <span> 2 </span>

### Array Loop Example
With array loop you can read @loop arrays and print them. 
You can define an array by `[ ]` and `|` between each value.

For example:

    @loop([Hello | World])
      p Lorem Ipsum
    
    @loop(Hello | World | !!, x)
      span x

HTML Output:

    <p> Lorem Ipsum </p>
    <p> Lorem Ipsum </p>
    <span> Hello </span>
    <span> World </span>
    <span> !! </span>

**Important Note:** You can use process commands inside your loops.

## @compile - When Python is not for you
Sometimes you want to run a code in a language of your choice between tags or something. @compile allows you to do it, but notice that it's a more advanced command.

### @compile structure

    @compile(file, compiled_file, compile_command, run_command)
    	CODE OF YOUR LANGUAGE
**file** = The file you want to write your code in. This file will be removed after it runs.
**compiled_file** = The file that you get when you run the compiler. In C language for example, the default file is a.out.
**compile_command** = The command that is used to compile the file.
**run_command** = The command that is used to run the file. The output of this command is the one that will appear on the HTML file.

### Example
Lets say that we want to write "Hello World", via C language in a title in our website. We are going to do it this way:

    h1
        @compile(file.c, a.out, gcc file.c, ./a.out)
        #include <stdio.h>
        int main() {
           printf("Hello, World!");
           return 0;
        }
Output:

    <h1> Hello, World! </h1>
 

**The next tutorial is saved for the hardest command of all. @eval.**

