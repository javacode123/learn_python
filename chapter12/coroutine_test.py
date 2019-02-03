# -*- coding: utf-8 -*-
"""
协程看上去也是一个子程序，在执行过程中可以被中断，执行其他的协程
众所周知，在计算机程序中 IO 操作会消耗大量的时间，但是在 IO 操作中
cpu 都是空闲的，造成资源浪费，可以使用协程，当有协程执行 IO 时可以去
执行其他的协程

线程 进程 协程：
    进程是操作系统划分空间的基本单位，每个进程会单独分配空间，进程之间切换需要消耗 cpu 资源
    线程是 cpu 调度的基本单位，一个进程可以有多个线程组成，且线程对于全局变量的操作需要加锁
    协程是在一个线程内部，协程之间是顺序执行，所以与线程相比不要加锁，且不需要消耗 cpu 进行调度
"""


# ----------- 通过协程实现生产者和消费者 -------------------
def consumer():
    r = ''
    while True:
        n = yield r  # 接收参数 r 返回参数 r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)  # c.send() 切换到 consumer 执行
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)  # 接收返回参数
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()  # 关闭 consumer


def consumer():
    r = ''
    while True:
        n = yield r  # 接收参数 r 返回参数 r
        if not n:
            return
        print('consumer consuming %s' % n)
        r = 'consumer return 200 OK'  # 返回值


def produce(c):
    c.send(None)  # 启动 consumer
    n = 1

    while n < 5:
        print('prducing %s' % n)
        r = c.send(n)  # 切换协程
        print(r)
        n = n + 1


c = consumer()
produce(c)