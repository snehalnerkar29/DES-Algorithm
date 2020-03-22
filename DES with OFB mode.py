from Crypto.Cipher import DES

from Crypto import Random

iv = Random.get_random_bytes(8)

des1 = DES.new(b'01234567', DES.MODE_OFB, iv)

des2 = DES.new(b'01234567', DES.MODE_OFB, iv)

text = 'Real faces are the new secrets'
text=pad(text)
text=str.encode(text)

cipher_text = des1.encrypt(text)

decipher_text=des2.decrypt(cipher_text)
print(cipher_text)
print(decipher_text)

#########
OUTPUT:
b'\xaf\x19\xac\xf7\x98\rr\xf2Ie\x95\xd8\xeaU\x04\xbcW\x8d\xbe\xd5\x95\x0f@gI1\xb9\xe5\x12_Y\x98'
b'Real faces are the new secrets  '
