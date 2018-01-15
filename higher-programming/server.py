#-*-coding: utf-8-*-
import socket
"""
服务端
我们使用 socket 模块的 socket 函数来创建一个 socket 对象。
socket 对象可以通过调用其他函数来设置一个 socket 服务。
现在我们可以通过调用 bind(hostname, port) 函数来指定服务的 port(端口)。
接着，我们调用 socket 对象的 accept 方法。该方法等待客户端的连接，并返回 connection 对象，表示已连接到客户端。
"""
# 创建socket对象
s = socket.socket()
# 获取本地主机名
host = socket.gethostname()
# 设置端口
port = 12345
# 绑定端口
s.bind((host,port))
# 等待客户端连接
s.listen(5)
while True:
    # 建立客户端连接
    c,addr = s.accept()
    print("连接地址: ",addr)
    c.send('欢迎访问菜鸟教程')
    # 关闭连接
    c.close()