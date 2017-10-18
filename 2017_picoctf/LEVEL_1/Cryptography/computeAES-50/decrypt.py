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