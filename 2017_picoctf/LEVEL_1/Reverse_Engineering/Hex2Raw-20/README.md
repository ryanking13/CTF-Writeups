## Hex2Raw - 20

### Description

This program requires some unprintable characters as input... But how do you print unprintable characters?

CLI yourself to /problems/f8c6dddd9de81e356e316ec9789288cd and turn that Hex2Raw!

### Hint

  - Google for easy techniques of getting raw output to command line. In this case, you should be looking for an easy solution.

### Write up

    $ ls
    flag  hex2raw  input

There are three files in the directory.

    $ ./hex2raw
    Give me this in raw form (0x41 -> 'A'):
    28fe16318f851d2f9de2b2ee90b55470

    You gave me:

We need to give some raw bytes as an input.

    $ python -c 'print "\x28\xfe\x16\x31\x8f\x85\x1d\x2f\x9d\xe2\xb2\xee\x90\xb5\x54\x70"' | ./hex2raw
    Give me this in raw form (0x41 -> 'A'):
    28fe16318f851d2f9de2b2ee90b55470

    You gave me:
    28fe16318f851d2f9de2b2ee90b55470
    Yay! That's what I wanted! Here be the flag:
    88980fa0253a3b711d54d64a94b1646c

Using python is an easy solution for generating raw bytes.

> 88980fa0253a3b711d54d64a94b1646c
