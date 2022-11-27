import threading
import time


def test1():
  for i in range(5):
    print("------test1-----%d" % i)
    time.sleep(1)
 

def main():
  #在调用thread之前先打印当前的线程信息
  print(threading.enumerate())
  t1 = threading.Thread(target=test1)

  #在调用thread之后打印当前的线程信息
  print(threading.enumerate())
  t1.start()

  #在调用start之后打印
  print(threading.enumerate())


#最后结论在t1.start之后才开启子线程
if __name__ == "__main__":
  main()
