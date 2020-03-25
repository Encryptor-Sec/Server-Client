import socket
def client():
    host = socket.gethostname()
    port = 5000 
    c = socket.socket()
    c.connect((host, port)) 
    message = input("Your Message : ") 
    while message.lower().strip() != 'bye':
        c.send(message.encode()) 
        data = c.recv(1024).decode()
        print('from server: ' + data) 
        message = input("Your Message ")
    c.close()
if __name__ == '__main__':
    client()
