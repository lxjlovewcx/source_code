import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#注意addr的格式为tuple类型的。
#以及tuple的两个元素为ip地址和端口号
#此处运行遇到错误，错误类型为OSError: [WinError 10013] 以一种访问权限不允许的方式做了一个访问套接字的尝试。
#原因是端口占用了。
sock.bind(("192.168.56.1", 8001))
print("已经绑定端口....")

# 监听
sock.listen()
print("正在监听中。。。")

#接受一个传进来的socket
skt, addr = sock.accept()
print("接受到一个socket")

#读取传入消息 ，实际是信息
#需要注意的是读取信息的长度一定要小于等于实际消息的长度，否则会假死
#因为socket会认为一定要接受相应的数据再返回，会出现socket一直等的情况。

msg = skt.recv(100)
print(type(msg))  #得出的是一个字节序列，字节流，因此需要解码

#decode编码，默认utf-8
print(msg.decode())

#给对方一个反馈
msg = "I love only wangchengxi"
skt.send(msg.encode())

skt.close()
sock.close()