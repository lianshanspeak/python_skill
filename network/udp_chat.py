import socket


def send_msg(udp_socket):
    """发送数据"""
    dest_ip = input("请输入对方的IP")
    dest_port = int(input("请输入对方的端口"))
    send_data = input("请输入要发送的数据")
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """接收数据"""
    recv_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_data[1]), recv_data[0].decode("utf-8")))


#main函数完成主要的主体控制
def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定信息
    udp_socket.bind(("",7788))
    # 循环处理事情
    print("XXXX聊天器")
    print("1.发送消息")
    print("2.接受消息")
    print("0.退出系统")
    while True:
        op = input("请输入功能")
        # 发数据
        if op == "1" :
            send_msg(udp_socket)
        #获取要发送的数据
        # dest_ip = input("请输入对方的IP")
        # dest_port = input("请输入对方的端口")
        # send_data = input("请输入要发送的数据")
        # udp_socket.sendto(send_data.encode("utf-8"),(dest_ip,dest_port))
        #接收数据并且显示
        elif op == "2" :
            recv_msg(udp_socket)
        elif op == "0" :
            break
        else:
            print("输入有误，请重新输入")
        # recv_data = udp_socket.recvfrom(1024)
        # print("%s:%s" %(str(recv_data[1]),recv_data[0].decode("utf-8")))
if __name__ == "__main__":
    main()