# Experiment 1: Breaking the Mono-alphabetic Substitution Cipher using  Frequency Analysis 


from collections import Counter

def frequency_analysis(cipher_text):
    cipher_text = cipher_text.lower()
    letters_only = [char for char in cipher_text if char.isalpha()]
    
    frequency = Counter(letters_only)
    sorted_frequency = frequency.most_common()
    
    return sorted_frequency

# Example usage
cipher_text = "wqx mrhvm eivhlm gspplki sj irkmrivvvmrk"
freq_result = frequency_analysis(cipher_text)

print("Cipher Text:", cipher_text)
print("\nLetter Frequency Analysis:")

for letter, count in freq_result:
    print(letter, ":", count)