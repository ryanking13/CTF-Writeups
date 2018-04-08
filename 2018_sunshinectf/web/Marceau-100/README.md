## Marceau - 100

### Description

> Hey my friend tells me that the flag is in this site's source code. Idk how to read that though, lol (🅱️retty lame tbh 😂)

> http://marceau.web1.sunshinectf.org

### Write up

> You specifically want my PHP source. Why did you accept anything else?

By fixing request headers `accept` parameter to `text/php`, the flag is obtained.

```
<?php
// sun{45k_4nd_y3_5h411_r3c31v3} (nice work!)

// */* won't work here- you'll have to be more assertive.
if(strpos($_SERVER['HTTP_ACCEPT'], "text/php") === false)
  echo "<marquee><h3>You specifically want my PHP source. Why did you accept anything else?</h3></marquee>";
else
  show_source(__FILE__);
?>
```

> sun{45k_4nd_y3_5h411_r3c31v3}
