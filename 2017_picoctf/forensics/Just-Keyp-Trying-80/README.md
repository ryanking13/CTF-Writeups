# Just Keyp Trying

> Here's an interesting capture of some data. But what exactly is this data? Take a look: data.pcap

- HINTS
> Find out what kind of packets these are. What does the info column say in Wireshark/Cloudshark?
> What changes between packets? What does that data look like?
> Maybe take a look at http://www.usb.org/developers/hidpage/Hut1_12v2.pdf

---

## Write-up

> $ tshark -r data.pcap -T fields -e usb.capdata > data.txt

* Inside of data.txt:

  00:00:09:00:00:00:00:00

  00:00:00:00:00:00:00:00

  00:00:0f:00:00:00:00:00

  00:00:00:00:00:00:00:00

  00:00:04:00:00:00:00:00

  00:00:00:00:00:00:00:00

  00:00:0a:00:00:00:00:00

  00:00:00:00:00:00:00:00

  ...

looks like we can use third column of data

Inside of 'Hut1_12v2.pdf' page 56, we can find Keyboard/Keypad table.

> ex) 09 > f

By mapping third column using the table, flag is achived

> flag{pr355_0nwards_cf9f010a}


* Similar CTF Problem

http://hexstr-morgan.blogspot.kr/2012/10/csaw-2012-net300-writeup.html
