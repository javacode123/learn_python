# -*- coding: utf-8 -*-
import multiprocessing
import threading

# 多个进程同一个变量，每个进程都会存储变量拷贝，因为每个进程都有自己的内存空间，进程之间通信可以通过文件
# 线程的空间是共享的，当然线程也有自己的作用域，但是对于进程内部的变量(线程共享)需要枷锁
# 假定这是你的银行存款:
balance = 0  # 全局变量
lock = threading.Lock()  # 锁


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    # 多线程同时执行会发生混乱，balance = balance + n 执行的时候分两步
    # 1: x = balance + n    2: balance = x 如果赋值的时候，线程1赋值过后，线程2立即赋值会出错
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(10):
        # 存取操作时先获取锁进行同步
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 释放锁
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(multiprocessing.cpu_count())
print(balance)