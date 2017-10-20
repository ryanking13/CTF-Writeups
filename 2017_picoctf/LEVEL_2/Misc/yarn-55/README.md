## yarn - 55

### Description

I was told to use the linux strings command on yarn, but it doesn't work. Can you help? I lost the flag in the binary somewhere, and would like it back

### Hint

  - What does the strings command use to determine if something is a string?
  - Is there an option to change the length of what strings considers as valid?

### Write up

    $ strings -n 3 yarn
    ...
    Sub
    mit
    _me
    _fo
    r_I
    _am
    _th
    e_f
    lag
    ...

> Submit_me_for_I_am_the_flag
