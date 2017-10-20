## Missing Identity - 100

### Description

Turns out, some of the files back from Master Challenge 1 were corrupted. Restore this one [file](./file) and find the flag. Update 16:26 EST 1 Apr If you feel that you are close, make a private piazza post with what you have, and an admin will help out. The flag starts with the character z.

### Hint

  - What file is this?
  - What do you expect to find in the file structure?
  - All characters in the file are lower case or numberical. There will not be any zeros.

### Write up

    $ file file
    file: data

file command says that the file is just a data.

But when we see it with hex editor, it looks like the signature of the file is corrupted.

    00000000: 5858 5858 5858 0000 0800 2344 7f4a 6a58  XXXXXX....#D.JjX
    00000010: bd98 b48c 0000 a58c 0000 0800 0000 666c  ..............fl

When we analyse the file with hex editor, we can find some file names.

    00068ff0: 006e 6f74 7468 6566 6c61 6735 2e70 6e67  .nottheflag5.png
    00069000: 504b 0102 1403 1400 0000 0800 2344 7f4a  PK..........#D.J
    00069010: 7663 94c0 f5c1 0000 19c2 0000 0f00 0000  vc..............
    00069020: 0000 0000 0000 0000 a481 9eda 0400 6e6f  ..............no
    00069030: 7474 6865 666c 6167 362e 706e 6750 4b01  ttheflag6.pngPK.
    00069040: 0214 0314 0000 0008 0023 447f 4aa7 207a  .........#D.J. z
    00069050: 1eac f100 0098 f100 000f 0000 0000 0000  ................
    00069060: 0000 0000 00a4 81c0 9c05 006e 6f74 7468  ...........notth
    00069070: 6566 6c61 6737 2e70 6e67 504b 0506 0000  eflag7.pngPK....

And the word `PK(\x50\x4b)` is a zip file signature.

It looks like that this file was a zip file.

So let's fix the corrupted signature to zip file signature.

    XX XX XX XX XX XX -> 50 4B 03 04 00 00

And by extracting the zip file, we get the flag

![flag](./flag.png)

> zippidydooda49688958
