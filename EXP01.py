from collections import Counter

def frequency_analysis(cipher_text):
    cipher_text = cipher_text.lower()
    # Filters out spaces and punctuation
    letters_only = [char for char in cipher_text if char.isalpha()]
    
    # Counts the frequency of each letter
    frequency = Counter(letters_only)
    
    # Sorts the letters based on frequency in descending order
    sorted_frequency = frequency.most_common()
    
    return sorted_frequency

# Example usage from the lab manual
cipher_text = "wqx mrhvm eivhlm gspplki sj irkmrivvvmrk"
freq_result = frequency_analysis(cipher_text)

print("Cipher Text:", cipher_text)
print("\nLetter Frequency Analysis:")
for letter, count in freq_result:
    print(letter, ":", count)
