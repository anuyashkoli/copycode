# Implement and design the product cipher using Substitution

def encrypt(text, key):
    cipher_text = ""

    for char in text:
        if char.isalpha():
            # preserve lowercase
            cipher_text += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            # keep space and other characters unchanged
            cipher_text += char

    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ""

    for char in cipher_text:
        if char.isalpha():
            plain_text += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
        else:
            plain_text += char

    return plain_text


# Input
plain_text = input("Enter the Plain Text: ").lower()
key = int(input("Enter the value of the key: "))

print("\n-----------------------------")
print("Plain Text :", plain_text)
print("Key :", key)

cipher = encrypt(plain_text, key)
print("Cipher Text :", cipher)

decrypted = decrypt(cipher, key)
print("Decrypted Text :", decrypted)
print("-----------------------------")






# hello world
# 3