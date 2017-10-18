## WorldChat - 30

### Description

We think someone is trying to transmit a flag over WorldChat. Unfortunately, there are so many other people talking that we can't really keep track of what is going on! Go see if you can find the messenger at shell2017.picoctf.com:44323. Remember to use Ctrl-C to cut the connection if it overwhelms you!

### Hint

  - There are cool command line tools that can filter out lines with specific keywords in them. Check out 'grep'! You can use the '|' character to put all the output into another process or command (like the grep process)

### Write up

    $ nc loclhost 44323
    ...
    08:57:05 flagperson: this is part 1/8 of the flag - 7c20
    ...

We can see there is a `flagperson` who outputs the flag.

    nc localhost 44323 | grep flagperson
    08:58:17 flagperson: this is part 1/8 of the flag - 7c20
    08:58:18 flagperson: this is part 2/8 of the flag - 77dc
    08:58:19 flagperson: this is part 3/8 of the flag - 26c1
    08:58:36 flagperson: this is part 4/8 of the flag - 6dc8
    08:58:40 flagperson: this is part 5/8 of the flag - 1acd
    08:58:45 flagperson: this is part 6/8 of the flag - e49c
    08:58:46 flagperson: this is part 7/8 of the flag - d563
    08:58:56 flagperson: this is part 8/8 of the flag - 0146

> 7c2077dc26c16dc81acde49cd5630146
