# -*- coding: utf-8 -*-
from multiprocessing import Process, Queue
import time, random, os


# 父进程创建子进程，子进程之间通过 queue 进行通信
def write(q):
    print('%s process write' % os.getpid())
    for c in ['a', 'b', 'c']:
        q.put(c)
        time.sleep(random.random() * 4)


def read(q):
    print('%s process read' % os.getpid())
    while True:
        value = q.get(True)
        print('get %s from queue' % value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q, ))  # 写进程
    pr = Process(target=read, args=(q, ))  # 读进程
    pw.start()
    pr.start()
    pw.join()  # 等待 pw 运行完毕
    pr.terminate()  # 中断
