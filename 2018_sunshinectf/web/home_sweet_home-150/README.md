## home sweet home - 150

### Description

> Looks like this site is doing some IP filtering.
That's very FORWARD thinking of them.

> http://web1.sunshinectf.org:50005

### Write up

The site responses that our address is not authenticated.

> X-Originating-IP: 127.0.0.1

> X-Forwarded-For: 127.0.0.1

by adding these two parameters in request header, we can bypass the access control.

#### Reference

> https://github.com/lucyoa/ctf-wiki/tree/master/web/ip-access-control
