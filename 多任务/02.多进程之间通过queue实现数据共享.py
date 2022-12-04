# encoding: utf-8
import multiprocessing


def download_from_web(q):
  #模拟从网上下载数据
  data = [11,22,33,44]
  #向队列里写入数据
  for temp in data:
    q.put(temp)
  print("-------下载器已经下载数据并且保存在队列中-----")


def analysis_data(q):
  waitting_data = list()
  #从队列中取数据
  while True:
    data = q.get()
    waitting_data.append(data)
    if q.empty():
      break 
  #模拟数据处理
  print(waitting_data)

def main():
  #1.创建一个队列
  q = multiprocessing.Queue()
  #2.创建多个进程将队列得引用当作实参传递到里面 
  p1 = multiprocessing.Process(target=download_from_web(q))
  p2 = multiprocessing.Process(target=analysis_data(q))
  p1.start()
  p2.start()







if __name__ == "__main__":
  main()
