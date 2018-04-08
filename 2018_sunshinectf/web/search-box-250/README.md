## Search box - 250

### Description

> This search engine doesn't look very secure.
Or well coded.
Or competent in any way shape or form.
This should be easy.

> Note: flag is in /etc/flag.txt

> http://search-box.web1.sunshinectf.org

### Write up

The site behaves like only google.com urls are allowed.

So we need to exploit the url parser.

By sending site[]=asdf, we can get error message which tells us that `parse_url()` is used.

In [A New Era Of SSRF](https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf), it can be found that other url parsers process url host differently from parse_url().

With some trial and error, it is found that

> ?site=http://@blahblah.com:@www.google.com/

by using this payload, we can get blahblah.com's source.

Now, instead of using http scheme, let's use file scheme to get local file.

> http://search-box.web1.sunshinectf.org/?site=file://@localhost:@www.google.com//etc/flag.txt%23

trailing %23(#) is needed because the server adds trailing slash(/) on every input.

> sun{R3quE5t_tyP3S_m4tT3r}
