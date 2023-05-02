import socket
import time
import threading

clients = []

def handler(client_sock, client_addr):
    while True:
        msg = client_sock.recv(1024)
        if 'quit' in msg.decode():
            sock.send(msg)
            print(f'{client_addr} is exited')
            clients.remove(client_sock)
            client_sock.close()
            break
        print(f'{time.asctime()} {client_addr}: {msg.decode()}')
        for sock in clients:
            if sock != client_sock:
                sock.send(msg)

svr_addr = ('localhost', 2500)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(svr_addr)
sock.listen()

print('Server Started')

while True:
    client_sock, client_addr = sock.accept()
    clients.append(client_sock)
    print(f'new client {client_addr}')
    th = threading.Thread(target=handler, args=(client_sock, client_addr))
    th.daemon = True
    th.start()
