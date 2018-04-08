## My secret stash - 100

### Description

> Do you like secrets? I like secrets! In fact, I LOVE SECRETS! But there's no way I'll ever share my secrets with you! Not in a million years! I don't share secrets with anyone! Okay, I might share one secret with you, but I've stashed it away somewhere you'll never think to find it!If you can dig up my secert stash I'll let you have it! How about that huh? Does that sound like a fun game? See if you can dig up my secret stash!hahahahahahahahahahahaha!!!!!!!!!!!!!!!!!!!!!!!!!!!!

### Write up

A git folder is given.

```
$ git log
...
+I feel like we are becoming good friends you and I. Yes. I even considered letting you in on one of my secrets just now, but I didn't want to risk it falling into the wrong hands. So instead I stashed it away and destroyed it so that no one would ever be able to recover my secrets! muahahahahahah!!!!!!
...
```

```
$ git reflog
3fe304a HEAD@{0}: commit: Bobby
92fb7e7 HEAD@{1}: commit: is
7e29273 HEAD@{2}: reset: moving to HEAD
7e29273 HEAD@{3}: commit (initial): vegan!
```

looks like the commit that contains flag is missing because of the reset.

```
$ git fsck
dangling commit 14a5c7088e7638abb2232c8cac1c7dd4687819f0
```

by `git fsck`, we can find dangling commit.

```
$ git reset --hard 14a5c708
WIP on master: 7e29273 vegan!
```

Reset to that commit. Flag retrieved.

> sun{git_gud_k1d}
