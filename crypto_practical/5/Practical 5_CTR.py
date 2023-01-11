from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b'secret data'

#Encryption
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CTR)
cipher_text = cipher.encrypt(data)
nonce = cipher.nonce
print("After Encryption:",cipher_text)

decrypt_cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
plain_text = decrypt_cipher.decrypt(cipher_text)
print("After Decryption:",plain_text)
