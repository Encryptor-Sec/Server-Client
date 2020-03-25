logo= '''\033[1;33
███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝
╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗
███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║
╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                 
'''
print(logo) 
import socket
def server():
    print('Waiting for client...')
    s = socket.socket()
    s.bind((socket.gethostname(),5000))
    s.listen(1)
    conn,address = s.accept()
    print("Connected To Client :- IP ->" + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("From Client : " + str(data))
        data = input('Your Message : ')
        conn.send(data.encode())
    conn.close()
if __name__ == '__main__':
    server()
