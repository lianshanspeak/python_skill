import socket

def main():
    #创建TCP套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 连接服务器
    # tcp_socket.connect("192.168.120.44","7789")
    service_ip = input("请输入要连接的服务IP")
    service_port = int(input("请输入要连接的port"))
    tcp_socket.connect((service_ip,service_port))
    # 发送/接收数据
    send_data = input("请输入要发送的数据")
    tcp_socket.send(send_data.encode("utf-8"))
    # 关闭套接字
    tcp_socket.close()
if __name__ == "__main__":
    main()