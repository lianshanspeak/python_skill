import socket

def main():
    # 创建套接字
    tcp_service_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 绑定IP和端口
    tcp_service_socket.bind(("",7890))
    # listen可以变为被动连接
    tcp_service_socket.listen(128)
    # accept等待客户的连接,返回值是一个元组
    print("*"*10)
    new_client_socket, client_addr = tcp_service_socket.accept()
    print("-"*10)
    print(client_addr)
    # recv/send接收发送数据
    recv_data = new_client_socket.recv(1024)
    print(recv_data)
    new_client_socket.send("hhhh".encode("utf-8"))
    #关闭套接字
    new_client_socket.close()
    tcp_service_socket.close()


if __name__ == "__main__":
    main()