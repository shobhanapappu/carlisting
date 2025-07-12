import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

class CredentialManager:
    def __init__(self, key=None):
        if key is None:
            self.key = Fernet.generate_key()
        else:
            self.key = key
        self.cipher_suite = Fernet(self.key)
    
    def encrypt_credential(self, text):
        """Encrypt a credential string"""
        if isinstance(text, str):
            text = text.encode()
        encrypted = self.cipher_suite.encrypt(text)
        return base64.urlsafe_b64encode(encrypted).decode()
    
    def decrypt_credential(self, encrypted_text):
        """Decrypt a credential string"""
        try:
            encrypted_bytes = base64.urlsafe_b64decode(encrypted_text.encode())
            decrypted = self.cipher_suite.decrypt(encrypted_bytes)
            return decrypted.decode()
        except Exception as e:
            print(f"Decryption error: {e}")
            return None
    
    def save_credentials(self, credentials_dict, filename="credentials.enc"):
        """Save encrypted credentials to file"""
        encrypted_data = {}
        for key, value in credentials_dict.items():
            encrypted_data[key] = self.encrypt_credential(value)
        
        with open(filename, 'w') as f:
            for key, encrypted_value in encrypted_data.items():
                f.write(f"{key}:{encrypted_value}\n")
    
    def load_credentials(self, filename="credentials.enc"):
        """Load and decrypt credentials from file"""
        credentials = {}
        try:
            with open(filename, 'r') as f:
                for line in f:
                    if ':' in line:
                        key, encrypted_value = line.strip().split(':', 1)
                        decrypted_value = self.decrypt_credential(encrypted_value)
                        if decrypted_value:
                            credentials[key] = decrypted_value
        except FileNotFoundError:
            print(f"Credentials file {filename} not found")
        return credentials 