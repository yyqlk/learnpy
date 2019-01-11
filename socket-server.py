
import os
import socket

server = socket.socket()
server.bind(('localhost',9999))  # 绑定地址端口
server.listen()  # 监听地址端口
print('start listen...')
while True:
    conn, addr = server.accept()  # conn是一个连接的实例，用来接通一个连接
    print('connect success,await ...')
    while True:
        data = conn.recv(1024)
        print('order:',data.decode())
        if not data:
            print('client failed')
            break              # 如果客户端关闭，会不断发送空包，所以如果是空包，就断开这个连接
        cmd_recv = os.popen(data.decode()).read()  # 接受字符串（字节先解码为字符创），输出字符串
        print('字符长度',len(cmd_recv))
        conn.send(str(len(cmd_recv)).encode('utf-8'))  # 发送消息大小给客户端
        conn.send(cmd_recv.encode('utf-8'))
        print('send done')
server.close()



