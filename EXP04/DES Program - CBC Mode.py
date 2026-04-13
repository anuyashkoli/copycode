from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

message = 'This is a long message for DES encryption practical.'
data = message.encode()

key = get_random_bytes(8)
cipher = DES.new(key, DES.MODE_CBC)
ciphertext = cipher.encrypt(pad(data, DES.block_size))

print('Encrypted:', ciphertext)

decipher = DES.new(key, DES.MODE_CBC, cipher.iv)
plaintext = unpad(decipher.decrypt(ciphertext), DES.block_size)

print('\nDecrypted:', plaintext.decode())
