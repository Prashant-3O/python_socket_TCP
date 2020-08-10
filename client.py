import socket


def client_program():
    host = socket.gethostname()
    port = 50011
    cs = socket.socket()
    cs.connect((host, port))
    message = input('->')
    while message.lower().strip() != 'exit':
        cs.send(message.encode())
        data = cs.recv(1024).decode()
        print('Received from server: ' + data)
        message = input("->")
    cs.close()
if __name__ == '__main__':
    client_program()
