# AUTHOR : YYQLK
import socket
import hashlib
client = socket.socket()
client.connect(('localhost',9999))  # 要连接的地址（ip和端口）
while True:
    cmd = input('>>:').strip()
    if len(cmd) == 0:
        continue
    if cmd.startswith('get'):
        client.send(cmd.encode())
        cmd_rev_size = client.recv(1024)  # 接受第一个数据，执行命令结果的长度
        print(cmd_rev_size)
        if cmd_rev_size != b"300":
            file_total_size = int(cmd_rev_size.decode())
            print(file_total_size)
            client.send(b"ready to recv file")
            receive_size = 0
            new_filename = input('save as：')
            f = open(new_filename, "wb")
            m = hashlib.md5()
            while receive_size < file_total_size:  # 如果一次收到的字符串长度没有达到服务器告诉我们的，我们就在接受一次，直到接受的字符串长度相等
                data = client.recv(1024)
                receive_size += len(data)  # data 是字节，解码成字符串
                f.write(data)
                m.update(data)
                last_file_size = file_total_size - receive_size
                if last_file_size < 1024:
                    data = client.recv(last_file_size)
                    f.write(data)
                    m.update(data)
                    receive_size += len(data.decode())
                print(file_total_size, receive_size)
            else:
                new_file_md5 = m.hexdigest()
                print('cmd res receive done...', receive_size)
                f.close()
            receive_md5 = client.recv(1024)
            print(new_file_md5, receive_md5)
        else:
            print("flie not exit")
client.close()

