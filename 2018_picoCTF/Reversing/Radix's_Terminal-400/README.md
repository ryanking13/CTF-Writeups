## Radix's Terminal - 400

### Description

> Can you find the password to Radix's login? You can also find the executable in /problems/radix-s-terminal_4_ae97ed559436608827a568341938c2a4?

### Write up

```
$ strings radix
...
cGljb0NURntiQXNFXzY0X2VOQ29EaU5nX2lTX0VBc1lfMTk1MTA2ODN9
...
```

```
$ echo 'cGljb0NURntiQXNFXzY0X2VOQ29EaU5nX2lTX0VBc1lfMTk1MTA2ODN9' | base64 -d
picoCTF{bAsE_64_eNCoDiNg_iS_EAsY_19510683}
```