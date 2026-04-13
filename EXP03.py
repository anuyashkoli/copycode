# -*- coding: utf-8 -*-
"""
Program to aid in the cryptanalysis of a Vigenère cipher.
"""
from math import gcd

def kasiski_examination(ciphertext):
    """
    Finds repeated sequences and calculates the GCD of their distances.
    This helps in determining the key length.
    """
    ciphertext = ciphertext.upper().replace(" ", "").replace(".", "")
    repeats = {}
    
    for i in range(len(ciphertext) - 2):
        sequence = ciphertext[i:i+3]
        if sequence in repeats:
            repeats[sequence].append(i)
        else:
            repeats[sequence] = [i]
            
    distances = []
    for seq, positions in repeats.items():
        if len(positions) > 1:
            for i in range(len(positions) - 1):
                distance = positions[i+1] - positions[i]
                distances.append(distance)
                
    if not distances:
        return "No significant repeated sequences found."
        
    # Calculate the GCD of all distances
    key_length = distances[0]
    for d in distances[1:]:
        key_length = gcd(key_length, d)
        
    return key_length, sorted(list(set(distances)))

def main():
    """
    Main function to get user input and display analysis results.
    """
    cipher = input("Enter the Vigenère ciphertext: ")
    print("\n--- Kasiski Examination Results ---")
    
    try:
        result = kasiski_examination(cipher)
        
        # Check if the function returned the error string or the actual data
        if isinstance(result, str):
            print(result)
        else:
            key_len, distances = result
            print(f"Possible Key Length: {key_len}")
            print(f"Distances between repeated sequences: {distances}")
            print(f"\nUsing the GCD, a probable key length of {key_len} is suggested. Next, perform frequency analysis on each sub-cipher.")
            
    except (TypeError, IndexError):
        print("Could not determine a probable key length. Ciphertext may be too short or complex.")

if __name__ == "__main__":
    main()
