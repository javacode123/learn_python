# -*- coding: utf-8 -*-
import time
import threading


# 线程运行代码, 进程是操作系统对空间分配的基本单位，线程是 cpu 调度的基本单位
# 一个进程一般有多个线程组成，对于由单核 cpu 的计算机来说，多线程只是相对来说
# 线程都是串行执行，操作系统用来操纵计算机的硬件资源，称为 '内核'，用户无法操作
# 防止系统崩溃，操作系统提供系统调用，应用程序针对不同系统提供的不同系统调用来开发应用程序
# 对于操作系统开发人员来说，不同硬件需要对应不同系统开发代码，总之就是分层开发的思想
# 对于跨平台的语言来说，它们针对不同平台有不同的虚拟机或者解释器，可以对编译后的代码进行执行
def loop():
    """ 线程执行代码 """
    print('thread %s is running ' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread is running operate %d' % n)
        time.sleep(1)
    print('thread %s is end' % threading.current_thread().name)


if __name__ == '__main__':
    t = threading.Thread(target=loop, name='thread1')
    t.start()  # 启动线程
    print('process is running')  # 主线程仍然执行
    t.join()  # 等待线程结束
    print('thread %s is end' % threading.current_thread().name, t.name)

