import os
import json
import base64
from Crypto.Cipher import AES
from googleapiclient.discovery import build

def setup_personal_data():
    personal_data = {
        "name": "Jeremy",
        "email": "jeremy.rich@berjak.com.au",
        "projects": ["Bear_Project", "Berjak_Project", "Zion_Project"]
    }
    key = b'Sixteen byte key'
    encrypted_data = encrypt(json.dumps(personal_data), key)
    save_personal_data('/users/jbear/documents/projects/Bear_Project/personal_data.json', encrypted_data)

def encrypt(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    return {
        'nonce': base64.b64encode(nonce).decode('utf-8'),
        'ciphertext': base64.b64encode(ciphertext).decode('utf-8'),
        'tag': base64.b64encode(tag).decode('utf-8')
    }

def save_personal_data(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    setup_personal_data()
    print("AI Personal Assistant setup complete.")
