#Encrypt long messages using various modes of operation using AES and DES.
# command for error 
# pip install pycryptodome

# aes (CBC Mode)
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

message = "This is a long message used for encryption in CNS practical."
data = message.encode()

key = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_CBC)
ciphertext = cipher.encrypt(pad(data, AES.block_size))

print("Encrypted:", base64.b64encode(ciphertext))

decipher = AES.new(key, AES.MODE_CBC, cipher.iv)
plaintext = unpad(decipher.decrypt(ciphertext), AES.block_size)

print("Decrypted:", plaintext.decode())










#Des cbc mode
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

message = "This is a long message for DES encryption practical."
data = message.encode()

key = get_random_bytes(8)

cipher = DES.new(key, DES.MODE_CBC)
ciphertext = cipher.encrypt(pad(data, DES.block_size))

print("Encrypted:", ciphertext)

decipher = DES.new(key, DES.MODE_CBC, cipher.iv)
plaintext = unpad(decipher.decrypt(ciphertext), DES.block_size)

print("Decrypted:", plaintext.decode())





# 3. AES (ECB Mode)
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

message = "This is a long message used for encryption in CNS practical."
data = message.encode()

key = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(data, AES.block_size))

print("Encrypted:", base64.b64encode(ciphertext))

decipher = AES.new(key, AES.MODE_ECB)
plaintext = unpad(decipher.decrypt(ciphertext), AES.block_size)

print("Decrypted:", plaintext.decode())








# 4. DES (ECB Mode)
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

message = "This is a long message for DES encryption practical."
data = message.encode()

key = get_random_bytes(8)

cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(pad(data, DES.block_size))

print("Encrypted:", ciphertext)

decipher = DES.new(key, DES.MODE_ECB)
plaintext = unpad(decipher.decrypt(ciphertext), DES.block_size)

print("Decrypted:", plaintext.decode())