from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 5555))
s.listen(5)
print('waiting...')

def calculate(equation):
    operators = ['+', '-', '*', '/']
    for operator in operators:
        if operator in equation:
            L, R = equation.split(operator)
            if operator == '+':
                return int(L) + int(R)
            elif operator == '-':
                return int(L) - int(R)
            elif operator == '*':
                return int(L) * int(R)
            elif operator == '/':
                return round(float(L) / float(R), 1)
    return None

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024).decode()
        if not data:
            break
        result = calculate(data)
        if result is not None:
            client.send(str(result).encode())
        else:
            client.send(b'Try again')

client.close()