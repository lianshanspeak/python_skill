import threading
import time

#定义一个全局变量
g_num = 0


def test1(num):
  global g_num
  #如果之前没有加锁，这里开始加锁，之前有锁的话就等待
  mutex.acquire()
  for i in range(num):
    g_num += 1
  #使用完之后释放锁
  mutex.release()
  print("-------in test1 g_num=%d" % g_num)

def test2(num):
  global g_num
  mutex.acquire()
  for i in range(num):
    g_num += 1
  mutex.release()
  print("-------in test2 g_num=%d" % g_num)

#创建一个互斥锁
mutex = threading.Lock()


def main():
  t1 = threading.Thread(target=test1(100000000))
  t2 = threading.Thread(target=test2(100000000))
  
  t1.start()
  t2.start()

  #等待上面的2个线程执行完
  print("-------in main Thread g_num =%d" % g_num)

if __name__ == "__main__":
  main()





