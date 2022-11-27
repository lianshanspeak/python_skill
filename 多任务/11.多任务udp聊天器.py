import threading
import socket






def recv_msg(udp_socket):
  """接收数据并显示数据"""
  while True:
    recv_data = udp_socket.recv(1024)
    print(recv_data)


def send_msg(udp_socket,dest_ip,dest_port):
  """发送数据"""
  while True:
    send_data = input("输入要发送的数据")
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip,dest_port))


def main():
  """完成udp聊天器的控制整体"""
  #创建套接字
  udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  #绑定端口和IP
  udp_socket.bind(("",7890))
  #输入目标机器的的端口和Ip
  dest_ip = input("目标机器的IP")
  dest_port = int(input("目标机器的port"))
 
  #接收和发送数据
 
  #创建两个线程去执行任务
  t_recv = threading.Thread(target=recv_msg(udp_socket))
  t_send = threading.Thread(target=recv_msg(udp_socket,dest_ip,dest_port))
  t_recv.start()
  t_send.start()


if __name__ == "__main__":
  main()

