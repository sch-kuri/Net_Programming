from socket import *
import random
import struct

HOST = ''
PORT = 9999

def generate_data():
    heartbeat = random.randint(40, 140)
    steps = random.randint(2000, 6000)
    cal = random.randint(1000, 4000)
    data = struct.pack('3i', heartbeat, steps, cal)
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