from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.serialization import (
    load_pem_private_key, load_pem_public_key,
    Encoding, PrivateFormat, PublicFormat, NoEncryption
)
import base64

def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    
    private_pem = private_key.private_bytes(
        encoding=Encoding.PEM,
        format=PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=NoEncryption()
    )
    
    public_pem = public_key.public_bytes(
        encoding=Encoding.PEM,
        format=PublicFormat.SubjectPublicKeyInfo
    )
    return private_pem, public_pem

def encrypt_RSA(public_key_pem, plaintext):
    public_key = load_pem_public_key(public_key_pem)
    ciphertext = public_key.encrypt(
        plaintext.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return base64.b64encode(ciphertext).decode()

def decrypt_RSA(private_key_pem, encrypted_text):
    private_key = load_pem_private_key(private_key_pem, password=None)
    ciphertext = base64.b64decode(encrypted_text)
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()

def sign_message(private_key_pem, message):
    private_key = load_pem_private_key(private_key_pem, password=None)
    signature = private_key.sign(
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return base64.b64encode(signature).decode()

def verify_signature(public_key_pem, message, signature):
    public_key = load_pem_public_key(public_key_pem)
    try:
        public_key.verify(
            base64.b64decode(signature),
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

if __name__ == "__main__":
    private_key, public_key = generate_keys()
    message = "Hello, I'm Anuyash from SIGCE"
    
    encrypted_text = encrypt_RSA(public_key, message)
    decrypted_text = decrypt_RSA(private_key, encrypted_text)
    
    signature = sign_message(private_key, message)
    is_valid = verify_signature(public_key, message, signature)
    
    print("Original Message:", message)
    print("\nEncrypted Message:\n[",encrypted_text,"]")
    print("\nDecrypted Message:", decrypted_text)
    print("\nDigital Signature:\n[",signature, "]")
    print("\nSignature Verification:", is_valid)
