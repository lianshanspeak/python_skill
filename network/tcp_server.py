import socket

def main():
    # 1.创建套接字
    tcp_service_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.绑定IP和端口
    tcp_service_socket.bind(("",7890))
    # 3.listen可以变为被动连接
    tcp_service_socket.listen(128)
    # 4.accept等待客户的连接,返回值是一个元组
    while True:
        print("等待一个新的客户端到来")
        new_client_socket, client_addr = tcp_service_socket.accept()
        print("一个新的客户端已经到来%s" % str(client_addr))

        while True:
        # recv/send接收发送数据
            recv_data = new_client_socket.recv(1024)

            # 如果recv_data解阻塞，那么有两种方式
            # 1.客户端发过来数据
            # 2.客户端调用了close导致recv解阻塞
            # 回送一部分数据给客户端
            # recv_data不为None,有数据
            if recv_data :
                new_client_socket.send("hhhh".encode("utf-8"))
                print("收到客户端的请求：%s" % recv_data.decode("utf-8"))
            else:
                print("用户已经断开连接")
                break
        #关闭套接字
        new_client_socket.close()
        print("已经服务完毕")
    #     如果将监听套接字关闭了，会导致不能再次等待客户端到来
    tcp_service_socket.close()


if __name__ == "__main__":
    main()