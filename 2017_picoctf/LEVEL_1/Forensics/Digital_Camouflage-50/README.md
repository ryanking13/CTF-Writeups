## Digital Camouflage - 50

### Description

We need to gain access to some routers. Let's try and see if we can find the password in the captured network data: [data.pcap](data.pcap).

### Hint

  - It looks like someone logged in with their password earlier. Where would log in data be located in a network capture?
  - If you think you found the flag, but it doesn't work, consider that the data may be encrypted.

### Write up

Open the pcap file with wireshark.

  - File -> Export Objects -> HTTP

We can see various html files are requested.

Inside of `main.html` file, we can see userid and pswrd parameter.

    userid=grassers&pswrd=cHJ2cUJaTnFZdw%3D%3D

pswrd is base64 encoded ( + URL encoded ).

By decoding it, we can get the flag.

> prvqBZNqYw
