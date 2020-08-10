import socket

def server_program():
    host = socket.gethostname()
    port = 50011
    ss = socket.socket() 
    ss.bind((host, port))
    ss.listen(2)
    conn, address = ss.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = input('->')
        conn.send(data.encode())
    conn.close()

if __name__ == '__main__':
    server_program()

