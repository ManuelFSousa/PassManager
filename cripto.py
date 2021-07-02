import os.path
from os import path
import cryptography

def check_key():
    if path.exists("key.key") == False:
        key = Fernet.generate_key()
        with open("key.key","wb") as key_file:
            key_file.write(key)

def load_key():
    return open("key.key","r").read()