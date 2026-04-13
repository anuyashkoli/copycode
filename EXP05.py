import hashlib
import hmac

print("----- Cryptographic Hash Function Demo -----")
message = input("Enter a message: ")
hash_object = hashlib.sha256(message.encode())
hash_value = hash_object.hexdigest()
print("SHA-256 Hash Value:", hash_value)
print("\n----- Avalanche Effect Demonstration -----")
message2 = input("Enter a slightly modified message: ")
hash_object2 = hashlib.sha256(message2.encode())

hash_value2 = hash_object2.hexdigest()
print("New SHA-256 Hash Value:", hash_value2)
print("\nObserve how a small change in the input produces a completely different hash.")
print("\n----- HMAC Generation -----")
key = input("Enter secret key: ")
hmac_result = hmac.new(key.encode(), message.encode(), hashlib.sha256)
print("Generated HMAC:", hmac_result.hexdigest())
