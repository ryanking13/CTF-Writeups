## Recovering From the Snap - 150

### Description

> There used to be a bunch of animals here, what did Dr. Xernon do to them?

### Write up

```
$ file animals.dd
animals.dd: DOS/MBR boot sector, code offset 0x3c+2, OEM-ID "mkfs.fat", sectors/cluster 4, root entries 512, sectors 20480 (volumes <=32 MB) , Media descriptor 0xf8, sectors/FAT 20, sectors/track 32, heads 64, serial number 0x9b664dde, unlabeled, FAT (16 bit)
```

It's a boot sector file.

```
./foremost animals.dd
```

foremost easily finds flag.
