## LeakedHashed - 90

### Description

Someone got hacked! Check out some service's password hashes that were leaked at hashdump.txt! Do you think they chose strong passwords? We should check... The service is running at shell2017.picoctf.com:3815!

### Hint

  - See if you can crack any of the login credentials and then connect to the service as one of the users. What's the chance these hashes have actually already been broken by someone else? Are there websites that host those cracked hashes? Connect from the shell with nc.

### Write up

    root:be3f7de032d2e398ec542a7df71e0417
    christene:89689941d40794e311ef8bc7061b9944
    nadia:8b1660cfc5ce8217cb9188cc6b652e91
    myra:8bb421ff32a77382408a6e1539855e40
    sharell:55cbbc70c9579b3459a3a68a04f8bb79

It looks like password is md5 hashed.

root password is not decryptable but other passswords like christene:89689941d40794e311ef8bc7061b9944 is decryptable by rainbow table attack.

    89689941d40794e311ef8bc7061b9944 MD5 : 7h1ck

So, let's connect to service.

    $ nc localhost 3815
    enter username:
    christene
    christene's password:7h1ck

Then we get the flag.

    ...
    /\__/\
    /`    '\
    === 0  0 ===
    \  --  /    - flag is 4f36a002cc953e6567a878758abc8cf9

    /        \
    /          \
    |            |
    \  ||  ||  /
    \_oo__oo_/#######o
    ...
