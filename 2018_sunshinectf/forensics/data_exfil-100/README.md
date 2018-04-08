## Data Exfil - 100

### Description

> We think a critical document has been stolen out of our network, luckily our next gen IDS managed to capture the traffic during the attack. Can you tell us what they took?

### Write up

pcap file and some log files (extracted from pcap) are given.

Inside of pcap file, there are bunch of DNS and HTTP packets

Some DNS packets goes to 8.8.8.8, which is definitely google DNS, and some goes to 54.175.216.124, which is unknown DNS service hmmm... :thinking_face:

By closely looking at DNS packets that goes to 54.175.216.214, it could be found that is asks strange address like

> 504b030414000000000030be774c973a10791e0000001e0000000a000000.cozybear.group

and the DNS service returns that all these addresses are resolved to 127.0.0.1.

Looks like 54.175.216.124 is the malicious attacker's server, and he is leaking data.

Let's see what data is leaking.

`504b` = `PK` is file signature of a zip fle. So by concatenating all this prefixes on url, we can retrieve a zip file, and inside that zip file, there is a flag.
