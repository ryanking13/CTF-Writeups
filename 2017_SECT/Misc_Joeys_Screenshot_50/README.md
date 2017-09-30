## Joeys Screenshot - 50

### Description

> Joey gave me this screenshot to prove he got into The Gibson. Can you help us hack The Gibson too?

### Write up

![](./chall.png)

png 파일 하나가 주어져있다.

hex 뷰어로 살펴보면,

```
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 046b 0000 01e1 0802 0000 0056 58a4  ...k.........VX.
00000020: d300 0000 2869 5458 7443 6f6d 6d65 6e74  ....(iTXtComment
00000030: 0001 0031 3333 3700 4330 7c56 7c7c 567c  ...1337.C0|V||V|
00000040: 337c 5c7c 3700 789c 8b37 3603 0001 bc00  3|\|7.x..76.....
00000050: c93e 9304 e900 0000 2869 5458 7443 6f6d  .>......(iTXtCom
00000060: 6d65 6e74 0001 0031 3333 3700 4330 7c56  ment...1337.C0|V
00000070: 7c7c 567c 337c 5c7c 3700 789c 3336 3207  ||V|3|\|7.x.362.
00000080: 0001 3700 9def 3d61 7b00 0000 2769 5458  ..7...=a{...'iTX
00000090: 7443 6f6d 6d65 6e74 0001 0031 3333 3700  tComment...1337.
000000a0: 4330 7c56 7c7c 567c 337c 5c7c 3700 789c  C0|V||V|3|\|7.x.
000000b0: 7336 0200 00ba 0076 98b6 5d64 0000 0028  s6.....v..]d...(
000000c0: 6954 5874 436f 6d6d 656e 7400 0100 3133  iTXtComment...13
000000d0: 3337 0043 307c 567c 7c56 7c33 7c5c 7c37  37.C0|V||V|3|\|7
000000e0: 0078 9c33 3436 0100 0130 0099 8d2c 7394  .x.346...0...,s.
000000f0: 0000 0028 6954 5874 436f 6d6d 656e 7400  ...(iTXtComment.
00000100: 0100 3133 3337 0043 307c 567c 7c56 7c33  ..1337.C0|V||V|3
00000110: 7c5c 7c37 0078 9c33 3532 0100 013a 009c  |\|7.x.352...:..
00000120: c834 2640 0000 0028 6954 5874 436f 6d6d  .4&@...(iTXtComm
00000130: 656e 7400 0100 3133 3337 0043 307c 567c  ent...1337.C0|V|
00000140: 7c56 7c33 7c5c 7c37 0078 9cf3 3332 0200  |V|3|\|7.x..32..
00000150: 0183 00b3 5156 a6e7 0000 0028 6954 5874  ....QV.....(iTXt
00000160: 436f 6d6d 656e 7400 0100 3133 3337 0043  Comment...1337.C
00000170: 307c 567c 7c56 7c33 7c5c 7c37 0078 9cf3  0|V||V|3|\|7.x..
00000180: 3031 0400 0174 00ae ebe5 5108 0000 0027  01...t....Q....'
00000190: 6954 5874 436f 6d6d 656e 7400 0100 3133  iTXtComment...13
```

`iTXtComment ---` 라는 문구가 계속 반복되는데, leet를 뜻하는 1337과 leet로 된 단어 comment(C0|V||V|3|\\|7)가 있는 걸 보면 대놓고 수상하다.

검색해보면 우선 `itxt`는 PNG의 메타데이터와 관계된 값이라고 한다.

구체적인 [구조](http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html)는 아래와 같다.

```
Keyword:             1-79 bytes (character string)
Null separator:      1 byte
Compression flag:    1 byte
Compression method:  1 byte
Language tag:        0 or more bytes (character string)
Null separator:      1 byte
Translated keyword:  0 or more bytes
Null separator:      1 byte
Text:                0 or more bytes
```

주어진 파일에서의 Text 영역을 모아보면 대체로 아래와 같은 형태의 hex 값을 갖고,

> 78 9C 8B 37 36 03 00 01 BC 00 C9 3E 93 04 E9 00 00 00 28

공통적으로 `78 9c`로 시작하는데, 이는 `zlib`의 파일 시그니쳐와 같다.

```python
import zlib

t = b'\x78\x9C\x33\x30\xB6\x00\x00\x01\x31\x00\x9C\x3B\x84\xDA\x81\x00\x00\x00\x28'
a = zlib.decompress(t)
print(a)

# b'038'
```

시험삼아 값 하나를 zlib으로 decompress해보면 실제로 숫자 값이 나오는 것을 확인할 수 있다.

그리고 모든 값을 다 파싱해서 출력해보면 다음과 같다.

```
['_36', '327', 'C2', '134', '524', 'N22', 'H41', '{4', '_11', '_33', '_13', '021', 'E1', '530', '342', 'H43', '038', '535', 'P26', 'U25', 'G37', '415', '39', 'B19', 'S0', 'U29', 'R28', 'R32', 'D14', '212', '_23', 'D5', 'D39', '_40', 'G17', 'K8', 'Y10', '344', '!45', '520', 'T3', '331', '118', '46', '}46', '_16']
```

`{`와 `}` 이 하나씩 있고, `_`도 섞여있으니 플래그인 것 같긴 한데, 순서가 뒤죽박죽이다.

살펴보면 첫자리가 알파벳, 특수기호 등이고 뒷 부분이 숫자인 형태다.

플래그의 포맷이 `SECT{...}`인데 `{4`가 있는 것을 보면 뒷 숫자가 인덱스를 뜻하는 것 같다.

따라서 재조립하는 스크립트를 작성한다.

```python
import re
import zlib
f = open('chall.png', 'rb').read()

checker = f[0x25:0x46]

comments = re.findall(b'iTXtComment[\s\S]*?(?=iTXt)', f)

fix = []
for c in comments:
	c = c[len(b'iTXtComment\x00\x01\x001337\x00C0|V||V|3|\\|7\x00'):]
	fix.append(c)

order = []
for f in fix:

	code = zlib.decompress(f).decode()
	order.append((int(code[1:]), code[0]))
	order.sort()

print(len(order))
for o in order:
	print(o[1], end='')

# SECT{D4K3Y_2_D4_G1B50N_5UP3RU53R_15_G0D_H3H3!}
```

regex로 파싱하는 것이 조금 불완전했는지, D4 와 K3Y 사이에 글자가 하나 더 들어가야 하는데 빠져있다.

그러나 leet를 해석하면 the key가 되므로 그냥 언더스코어를 넣어주면 된다.

> SECT{D4_K3Y_2_D4_G1B50N_5UP3RU53R_15_G0D_H3H3!}
