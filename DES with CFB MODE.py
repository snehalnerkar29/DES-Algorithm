def pad(text):
    while len(text)%8!=0:
        text+=' '
        
    return text
from Crypto.Cipher import DES

from Crypto import Random

iv = Random.get_random_bytes(8)

des1 = DES.new(b'01234567', DES.MODE_CFB, iv)

des2 = DES.new(b'01234567', DES.MODE_CFB, iv)

text = 'Real faces are the new secrets'
text=pad(text)
text=str.encode(text)

cipher_text = des1.encrypt(text)

decipher_text=des2.decrypt(cipher_text)
print(cipher_text)
print(decipher_text)
OUTPUT:


b'\x8f\x11n8\xc0?=\x8b\xf1Q\xca\x88{_\x9e\x98\xda\xb9TM\x977\xef:y\xb7>J\x7f\x8f5\xac'
b'Real faces are the new secrets  '
