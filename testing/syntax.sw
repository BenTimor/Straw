head
    ^set(websitename) Hello World GUYS
    ^set({text}) Hey my name is Ben and I'm testing
    title websitename
    @safe style(type="text/css")
        h1 {
            color: red;
        }
body
    @compile(file.c, a.out, gcc file.c, ./a.out)
        #include <stdio.h>
        int main() {
           // printf() displays the string inside quotation
           printf("Hello, World!");
           return 0;
        }

    h1 websitename
    p {text}
    @loop(5, b)
        p b
    @loop([ben,,bar | shay | bar], i)
        p i