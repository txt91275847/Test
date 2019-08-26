import threading
import time


class MyThread(threading.Thread):
    def __init__(self, threadId, threadName, delay):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.threadName = threadName
        self.delay = delay

    def run(self):
        print("开始线程:", self.threadName)
        print_time(self.threadName, 5, self.delay)
        print("退出线程:", self.threadName)


def print_time(threadName, counter, delay):
    while counter:
        time.sleep(delay)
        print(threadName, time.ctime(time.time()))
        counter = counter - 1


thread1 = MyThread(1, "Thread-1", 2)
thread2 = MyThread(2, "Thread-2", 1)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程！")


