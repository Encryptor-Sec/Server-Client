import socket
def server():
    s = socket.socket()
    s.bind((socket.gethostname(),5000))
    s.listen(1)
    conn,address = s.accept()
    print("Connected To :- " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from client : " + str(data))
        data = input('Your Message : ')
        conn.send(data.encode())
    conn.close()
if __name__ == '__main__':
    server()
