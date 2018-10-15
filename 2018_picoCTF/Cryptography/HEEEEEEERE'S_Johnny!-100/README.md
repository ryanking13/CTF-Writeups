## HEEEEEEERE'S Johnny! - 100

### Description

> Okay, so we found some important looking files on a linux computer. Maybe they can be used to get a password to the process. Connect with nc 2018shell1.picoctf.com 42165. Files can be found here: passwd shadow.

### Write up

passwd and shadow file is given.

John the ripper can be used to crack password.

```
./unshadow passwd shadow > out
./john out
...
kissme           (root)
...
```