## Puzzlingly Accountable - 100

### Description

We need to find a password. It's likely that the updated passwords were sent over the network. Let's see if that's true: [data.pcap](./data.pcap).

Update 16:26 EST 1 Apr If you feel that you are close, make a private piazza post with what you have, and an admin will help out. The ones and sevens unfortunately look like each other.

### Hint

  - How does an image end up on your computer? What type of packets are involved?

### Write up

By carefully analysing the pcap file, we can find there are 4 `GET /secret/blahblah.png` requests.

But following HTTP stream of that request in Wireshark doesn't gives us PNG file.

Instead, following TCP stream gives us the PNG file.

Each PNG file is part of the flag, and we can get the flag by concatenating it.

![./flags/flag.png](./flags/flag.png)

> 4b9b1f55f48a9a1b7e9e264f7f4b33a3
