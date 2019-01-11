# AUTHOR : YYQLK
import socket
client = socket.socket()

client.connect(('localhost',9999))  # 要连接的地址（ip和端口）

while True:
    cmd = input('>>:').strip()
    if len(cmd) == 0:
        continue
    client.send(cmd.encode('utf-8'))
    cmd_rev_size = client.recv(1024)  # 接受第一个数据，执行命令结果的长度
    print(cmd_rev_size.decode())
    recive_size = 0
    recive_data = ''
    while recive_size < int(cmd_rev_size.decode()):  # 如果一次收到的字符串长度没有达到服务器告诉我们的，我们就在接受一次，直到接受的字符串长度相等
        data = client.recv(1024)
        recive_size += len(data.decode())  # data 是字节，解码成字符串
        recive_data += data.decode()
    print('cmd res recive done...',recive_size)
    print(recive_data)
client.close()