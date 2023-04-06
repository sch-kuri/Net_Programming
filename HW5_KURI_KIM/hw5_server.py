from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    filename = req[0].split()[1][1:]

    try:
        if filename == 'index.html':
            f = open(filename, 'r', encoding='utf-8')
            mimeType = 'text/html; charset=utf-8'
        elif filename == 'iot.png':
            f = open(filename, 'rb')
            mimeType = 'image/png'
        elif filename == 'favicon.ico':
            f = open(filename, 'rb')
            mimeType = 'image/x-icon'
        else:
            raise FileNotFoundError

        res = 'HTTP/1.1 200 OK\r\n'
        res += 'Content-Type: {}\r\n'.format(mimeType)
        res += '\r\n'
        c.send(res.encode())

        if filename == 'index.html':
            data = f.read().encode('utf-8')
            c.send(data)
        else:
            data = f.read()
            c.send(data)

        f.close()

    except FileNotFoundError:
        res = 'HTTP/1.1 404 Not Found\r\n'
        res += '\r\n'
        res += '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'
        res += '<BODY>Not Found</BODY></HTML>'
        c.send(res.encode())

    c.close()
