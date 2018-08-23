#coding=utf-8
# import threading
# import time

# class MyThread(threading.Thread):
#     # 重写 构造方法
#     def __init__(self,num,sleepTime):
#         threading.Thread.__init__(self)
#         self.num = num
#         self.sleepTime = sleepTime

#     def run(self):
#         self.num += 1
#         time.sleep(self.sleepTime)
#         print('线程(%s),num=%d'%(self.name, self.num))

# if __name__ == '__main__':
#     mutex = threading.Lock()
#     t1 = MyThread(100,5)
#     t1.start()
#     t2 = MyThread(200,1)
#     t2.start()
from threading import Thread
import time

g_num = 0

def test1():
    global g_num
    for i in range(1000000):
        g_num += 1

    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num
    for i in range(1000000):
        g_num += 1

    print("---test2---g_num=%d"%g_num)


p1 = Thread(target=test1)
p1.start()

# time.sleep(3) #取消屏蔽之后 再次运行程序，结果会不一样，，，为啥呢？

p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)