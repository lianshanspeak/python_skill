# encoding: utf-8
from multiprocessing import Pool

import os,time, random


def worker(msg):
  t_start = time.time()
  print("%s开始执行，进程号为%d" % (msg,os.getpid()))
  #random.random()随机生成0~1之间的浮点数
  time.sleep(random.random()*2)
  t_stop = time.time()
  print(msg,"执行完毕，耗时%d" % int(t_stop - t_start))


po = Pool(3) #定义一个进程池，最大进程为3
for i in range(0,10):
  # Pool.apply_async(要调用的目标,(传递给目标的参数元组,))
  # 每次循环都会用空闲的子进程去调用目标
  po.apply_async(worker,(i,))


print("-----start-----")
#关闭进程池
po.close()
#等待进程池中的任务结束之后在执行后面的,必须放在close语句之后
po.join()
print("-----end-------")


  



