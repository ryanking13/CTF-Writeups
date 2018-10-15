## admin panel - 150

### Description

> We captured some traffic logging into the admin panel, can you find the password?

### Write up

pcap file is given, it's a HTTP traffic, not encrypted.

By exporting all HTTP objects using wireshark, login data can be retrieved.

```
user=admin&password=picoCTF{n0ts3cur3_894a6546}
```
