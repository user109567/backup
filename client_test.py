import socket

def main():
    host = "192.168.1.8"
    port = 9002
    s = socket.socket(socket.AF_INET, socket-SOCK_STREAM)
    s.connect((host, port))
    message = "Hello Server"

    while True:
        s.send(message.encode("ascii"))
        data = s.recv(1024)
        data = str(data.decode("ascii"))
        print(f"Server message: {data}")

        ans = input("Continue?: ")
        if ans == "y":
            continue
        else:
            break
    s.close()

if __name__ == "__main__":
    main()
