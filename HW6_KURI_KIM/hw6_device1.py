from socket import *
import random
import struct

HOST = ''
PORT = 8888

def generate_data():
    temp = random.randint(0, 40)
    humid = random.randint(0, 100)
    iilum = random.randint(70, 150)
    data = struct.pack('3i', temp, humid, iilum)
    return data

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            elif data == b"Request":
                response = generate_data()
                conn.sendall(response)
            elif data == b"quit":
                break
