from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b'secret data'

key = b'Sixteen byte key'
#Encryption 
cipher = AES.new(key, AES.MODE_CBC)
cipher_text = cipher.encrypt(pad(data, AES.block_size))
iv = cipher.iv
print("After Encryption:",cipher_text)

decrypt_cipher = AES.new(key, AES.MODE_CBC, iv)
plain_text = decrypt_cipher.decrypt(cipher_text)
print("After Decryption",plain_text)
