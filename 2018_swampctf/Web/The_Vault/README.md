## The Vault

### Description

> Has it been days? Weeks? You can't remember how long you've been standing at the door to the vault.
You can't remember the last time you slept
or ate,
or had a drop of water, for that matter.
But all of that is insignificant, in the presence of the untold fortunes that must lie just beyond the threshold.
> But the door. It won't budge. It says it will answer only to the DUNGEON_MASTER.
Have you not shown your worth?
But more than that,
It demands to know your secrets.
> Nothing you've tried has worked.
You've pled, begged, cursed, but the door holds steadfast, harshly judging your failed requests.
But with each failed attempt you start to notice more and more
that there's something peculiar about the way the door responds to you.
Maybe the door knows more than it's letting on.
...Or perhaps it's letting on more than it knows?

> NOTE: DO NOT USE AUTOMATED TOOLS
Connect
http://chal1.swampctf.com:2694

### Write up

There is a login page, and a message that only DUNGEON_MASTER can enter.

When I submitted the form, it made a POST request to

```
http://chal1.swampctf.com:2694/login/<id>.<secret>
```

So, when I tried to login as a

> ID: DUNGEON_MASTER

> SECRET: a

it showed message like this.

```
http://chal1.swampctf.com:2694/login/DUNGEON_MASTER.a

test_hash [ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb] does not match real_hash[40f5d109272941b79fdf078a0e41477227a9b4047ca068fff6566104302169ce]
```

The test hash was a SHA256 hash of 'a', which is the secret I send.

And the real hash was a SHA256 hash of `smaug123`.


http://chal1.swampctf.com:2694/login/DUNGEON_MASTER.smaug123

> flag{somewhere_over_the_rainbow_tables}
