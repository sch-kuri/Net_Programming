from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 5555))

while True:
    msg = input('Input (Ex: 20 + 17): ')
    if msg == 'q':
        break
    
    s.send(msg.encode())
    
    print('Received message:', s.recv(1024).decode())

s.close()