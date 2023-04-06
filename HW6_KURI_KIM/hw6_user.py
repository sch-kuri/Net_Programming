from socket import *
import sys
import time
import struct

# 소켓 생성
s1 = socket(AF_INET, SOCK_STREAM)
s2 = socket(AF_INET, SOCK_STREAM)

try:
    s1.connect(('localhost', 8888))
    print('IoT Device 1 is connected.')
    s2.connect(('localhost', 9999))
    print('IoT Device 2 is connected.')
except Exception as e:
    print(e)
    sys.exit()

while True:
    command = input("Enter the IoT Device Number! (1: Device 1, 2: Device 2, quit: End): ")
    if command == 'quit':
        break
    
    elif command == '1':
        s1.send(b'Request')
        data = s1.recv(12)
        if not data:
            print('IoT Device 1 data is not received.')
            continue
        else:
            timestamp = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())
            temp, humid, iilum = struct.unpack('3i', data)

            with open('data.txt', 'a') as f:
                f.write(f"{timestamp}: Device1: Temp={temp}, Humid={humid}, Iilum={iilum}\n")
                print(f"[{timestamp}: IoT Device 1: Temp = {temp}, Humid = {humid}, Iilum = {iilum}] - Data Saved")
                
    elif command == '2':
        s2.send(b'Request')
        data = s2.recv(12)
        if not data:
            print('IoT Device 2 data is not received.')
            continue
        else:
            timestamp = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())
            heartbeat, steps, cal = struct.unpack('3i', data)
 
            with open('data.txt', 'a') as f:
                f.write(f"{timestamp}: Device2: Heartbeat={heartbeat}, Steps={steps}, Cal={cal}\n")
                print(f"[{timestamp}: IoT Device 2: Heartbeat = {heartbeat}, Steps = {steps}, Cal = {cal}] - Data Saved")
                
    else:
        print('Invalid input. Please Enter Again.')
        continue

s1.send(b'quit')
s2.send(b'quit')