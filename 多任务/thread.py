import time
import threading


def sing():
    """唱歌5秒"""
    for i in range(5):
        print("-----唱的菊花台-----")
        time.sleep(1)


def dance():
    """跳舞5秒"""
    for i in range(5):
        print("-----正在跳舞-----")
        time.sleep(1)


def main():
    # Thread(target=sing)是一个对象，之后启动这个对象。t1叫做实例对象
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()