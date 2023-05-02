import socket
import threading

def receive_handler(sock):
    while True:
        msg = sock.recv(1024)
        if msg:
            print(msg.decode())

svr_addr = ('localhost', 2500)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_id = input('ID를 입력하세요: ')
sock.connect(svr_addr)
sock.send(('[' + my_id + ']').encode())

receive_thread = threading.Thread(target=receive_handler, args=(sock,))
receive_thread.daemon = True
receive_thread.start()

while True:
    msg = '[' + my_id + '] ' + input()
    sock.send(msg.encode())
