# -*- coding: utf-8 -*-
from multiprocessing import Pool
import os, time, random


# 当需要大量的进程时需要使用进程池来管理进程
def long_time_task(name):
    print('run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 4)
    end = time.time()
    print('run task use %0.2f' % (end-start))


if __name__ == '__main__':
    print('parent process is %s' % os.getpid())
    p = Pool(4)

    for i in range(10):  # 全局共有四个进程，当有进程空闲时继续往下执行
        p.apply_async(long_time_task, args=(i,))

    print('wait all subprocess done')
    p.close()
    p.join()  # 等待子进程结束继续执行
    print('all subprocess done')
