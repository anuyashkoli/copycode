#Cryptanalysis of Playfair and Vigenère Ciphers

from math import gcd

def kasiski_examination(ciphertext):
    ciphertext = ciphertext.upper().replace(" ", "")
    repeats = {}

    # check sequences of length 3
    for i in range(len(ciphertext) - 2):
        sequence = ciphertext[i:i+3]

        if sequence not in repeats:
            repeats[sequence] = []
        repeats[sequence].append(i)

    distances = []

    for seq, positions in repeats.items():
        if len(positions) > 1:
            for i in range(len(positions) - 1):
                distances.append(positions[i+1] - positions[i])

    if len(distances) == 0:
        return "No repeated sequences found"

    key_length = distances[0]
    for d in distances[1:]:
        key_length = gcd(key_length, d)

    return key_length, distances


cipher = input("Enter ciphertext: ")
result = kasiski_examination(cipher)

print(result)


#hellohellohello