import socket
EOL1 = '\n\n'
EOL2 = '\n\r\n'
body = '''hello world,from the fire.'''
response_params = [
    'HTTP/1.0 200 OK',
    'Date: Sun,27 may 2018 01:01:01 GMT',
    'Content-Type: text/html;charset=utf-8',
    'Content-Length: {}\r\n'.format(len(body.encode())),
    body
]
response = '\r\n'.join(response_params)
def handle_connect(conn, addr):
    request = ''
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)
    print(request)
    conn.send(response.encode())
    conn.close()


def main():
    serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    serversocket.listen(1)
    print('http://127.0.0.1:8000')
    try:
        while True:
            conn, address = serversocket.accept()
            handle_connect(conn,address)
    finally:
        serversocket.close()
if __name__ == '__main__':
    main()