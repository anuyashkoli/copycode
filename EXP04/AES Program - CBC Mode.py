from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

message = "This is a long message used for encryption in Cryptography and Network Security practical."
data = message.encode()

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC)
ciphertext = cipher.encrypt(pad(data, AES.block_size))

print('Encrypted:', base64.b64encode(ciphertext))

decipher = AES.new(key, AES.MODE_CBC, cipher.iv)
plaintext = unpad(decipher.decrypt(ciphertext), AES.block_size)

print('\nDecrypted:', plaintext.decode())
