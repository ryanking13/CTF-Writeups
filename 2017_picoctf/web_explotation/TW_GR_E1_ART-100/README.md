# TW_GR_E1_ART
> Oh, sweet, they made a spinoff game to Toaster Wars! That last room has a lot of flags in it though. I wonder which is the right one...? Check it out here.

- HINTS
> I think this game is running on a Node.js server. If it's configured poorly, you may be able to access the server's source. If my memory serves me correctly, Node servers have a special file that lists dependencies and a start command; maybe you can use that file to figure out where the other files are?

## Write-up

The file that contains dependencies and start command in Node.js is 'package.json'

So, by going to http://shell2017.picoctf.com:55830/package.json and by keep exploring,
it can be found that there are some files like
- /server/serv.js
- /server/game.js
- /server/config.js

Inside of game.js, we can see the item option 'revealFlag' that shows flag,

>case "revealFlag":

>  if (entity.items[action.item].effects[i].check == 64) {
    outcome.flag = process.env["PICO_CTF_FLAG"];
  }

So what is 'check' option?

When we see top of the config.js file, we can see 'createFlag' function which sets the check value.

And at the same file, we can see the code that generates multiple flag items with differenct check, location.

- flag{at_least_the_world_wasnt_destroyed_by_a_meteor_842aea1de69aa7c4069e8aae8815d22b}
