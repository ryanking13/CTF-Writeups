## computeAES - 50

### Description

You found [this](./clue.txt) clue laying around. Can you decrypt it?

### Hint

  - Try online tools or python

### Write up

Write a python [script](./decript.py) for decrypting AES_ECB cipher.

```python
import base64
from Crypto.Cipher import AES

def decrypt(enc, password):
	enc = base64.b64decode(enc)
	password = base64.b64decode(password)
	
	cipher = AES.new(password, AES.MODE_ECB)

	return cipher.decrypt(enc)

ciphertext = "rvn6zLZS4arY+yWNwZ5YlbLAv/gjwM7gZJnqyQjhRZVCC5jxaBvfkRapPBoyxu4e"
key = "/7uAbKC7hfINLcSZE+Y9AA=="

print decrypt(ciphertext, key)
```

> flag{do_not_let_machines_win_82e02651}
