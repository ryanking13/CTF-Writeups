## Aca-Shell-A - 150

### Description

> It's never a bad idea to brush up on those linux skills or even learn some new ones before you set off on this adventure! Connect with nc 2018shell1.picoctf.com 42334.

### Write up

It's a problem using basic linux commands.

```
cd secret
rm intel*
echo 'Drop it in!'
cd ../executables
./dontLookHere
whoami
cd ..
cp /tmp/TopSecret passwords
cd passwords
cat TopSecret
```
