import threading
import time
exitFlag = 0
# 继承父类threading.Thread
class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadId = threadID
        self.name = name
        self.counter = counter
    # 把要执行的代码写到 run 函数里面 线程在创建后会直接运行 run 函数
    def run(self):
        print("starting" +self.name)
        print_time(self.name,self.counter,5)
        print_time("Exiting"+self.name)

def print_time(threadname,delay,counter):
    while counter:
        if exitFlag:
            threading.Thread.exit()
        time.sleep(delay)
        print("%s: %s" %(threadname,time.ctime(time.time())))
        counter-=1
thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(2,"Thread-2",2)
thread1.start()
thread2.start()
print("Exiting main Thread")