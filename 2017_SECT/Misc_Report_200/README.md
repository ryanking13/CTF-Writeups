## Report - 200

### Description

> Mr. Belford sucks, is he hiding something....

### Write up

압축파일을 열어보면 pdf 파일이 있다.

pdf 뷰어로 열어보면 내용은 대화내역인 것 같다.

hex 뷰어로 살펴봐도 특별히 티나게 숨겨진 값은 없어보인다.

그러다가 눈에 띈 것이 마지막 부분의 `xref` 테이블이다.

```
xref
0 146
0000000000 65535 f
0000013999 00000 n
0000000019 00000 n
0000001039 00000 n
0000022799 00000 n
0000014372 00000 n
0000014507 0007d n
0000014635 00000 n
0000014772 00000 n
0000014900 00059 n
0000015028 00000 n
0000015164 00000 n
0000015293 00000 n
...
```

> A PDF consists of lots of COS objects and this tells you where they are located in the file

[검색](https://blog.idrsolutions.com/2011/05/understanding-the-pdf-file-format-%E2%80%93-pdf-xref-tables-explained/)해서 살펴보면 PDF 파일의 xref 테이블은 여러 오브젝트가 위치를 레퍼런스해주는 기능을 한다고 하는데,

앞의 두 숫자는 각각 오브젝트의 `offset`과 `generation number`를 나타낸다고 한다.

이 때 `generation number`란 pdf 파일을 수정하면서 해당 오브젝트가 몇번이나 바뀌었는가를 나타내는 값이라고 한다.

그런데 살펴보면 눈에 띄는 것이, 대부분의 `generation number` 값은 00000인데, 중간에 띄엄띄엄 0007d, 00059 같은 큰 값이 있다.

그리고 7D의 ASCII 값은 `}`다. 플래그의 느낌이 난다.

중간에 나오는 숫자들의 ASCII 값을 출력해주는 스크립트를 작성하였다.

```python
lines = open('xref.txt', 'r').readlines()

lines = [l.split()[1][3:] for l in lines]

flag = ''

for l in lines:
	if l == '00':
		continue

	flag = chr(int(l, 16)) + flag

print(flag)

# SECT{N07_N1C3_T0_BR3AK_LUCY}
```

빙고!

> SECT{N07_N1C3_T0_BR3AK_LUCY}
