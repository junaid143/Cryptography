
# working


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b'secret data'

#Encryption
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CFB)
cipher_text = cipher.encrypt(data)
iv = cipher.iv
print("After Encryption:", cipher_text)

#Decryption
decrypt_cipher = AES.new(key, AES.MODE_CFB, iv=iv)
plain_text = decrypt_cipher.decrypt(cipher_text)
print("After decryption:", plain_text)
