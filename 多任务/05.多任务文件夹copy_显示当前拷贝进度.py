# encoding: utf-8

import os
import multiprocessing


def copy_file(q,file_name,old_folder_name,new_folder_name):
  """完成文件复制"""
  old_f = open(old_folder_name + "/" + file_name,"rb")
  content = old_f.read()
  old_f.close()

  new_f = open(new_folder_name + "/" + file_name,"wb")
  new_f.write(content)
  new_f.close()
  # 如果拷贝完了，就像消息队列写一个消息，表示已完成
  q.put(file_name)  


def main():
  #1.获取用户要copy的文件夹的名字
  old_folder_name = input("请输入文件夹名字: ")
  #2.创建一个新的文件夹
  print(old_folder_name)
  try:
     new_folder_name = old_folder_name + "[附件]"
     os.mkdir(new_folder_name)
  except:
    pass
   #3.获取文件夹所有待copy的文件名字 listdir()
  file_names = os.listdir(old_folder_name)
 #
   #4.创建进程池
  po = multiprocessing.Pool(5)
   #5.创建一个队列
  q = multiprocessing.Manager().Queue()
   #6.向进程池中添加copy文件的任务
  for file_name in file_names:
    po.apply_async(copy_file(q,file_name, old_folder_name,new_folder_name))
  
  po.close()
  #po.join()
  #检测文件个数
  all_file_num = len(file_names)
  copy_ok_num = 0
  while True:
    file_name = q.get()
    #print("已经完成%s的拷贝" %file_name)
    copy_ok_num+=1
    print("\r拷贝完成度%.2f%%" % (copy_ok_num*100/all_file_num),end=" ")
    if copy_ok_num >= all_file_num:
      break
  print("")

if __name__ == "__main__":
  main()

