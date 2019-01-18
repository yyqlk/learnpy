# AUTHOR : YYQLK
import os
import socket
import hashlib

server = socket.socket()
server.bind(('localhost',9999))  # 绑定地址端口
server.listen()  # 监听地址端口
print('start listen...')
while True:
    conn, addr = server.accept()  # conn是一个连接的实例，用来接通一个连接
    print('connect success,await ...')
    while True:
        data = conn.recv(1024)
        print('order:', data.decode())
        if not data:
            print('client failed')
            break              # 如果客户端关闭，会不断发送空包，所以如果是空包，就断开这个连接
        cmd, filename = data.decode().split()  # 接受字符串（字节先解码为字符串），输出字符串
        print('filename',filename)
        if os.path.isfile(filename):
            f = open(filename, 'rb')
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            print('file_size', file_size)
            conn.send(str(file_size).encode())  # 发送消息大小给客户端
            ack = conn.recv(1024)  # wait for ack
            print(ack)
            for line in f:
                conn.send(line)
                m.update(line)
            f.close()
            conn.send(m.hexdigest().encode())
            print('md5', m.hexdigest())
        else:
            conn.send(b'300')
        print('send done')
server.close()
