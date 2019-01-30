# -*- coding: utf-8 -*-

from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    # 进程执行的函， 函数参数
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join(7)
    print('Child process end.')



# 获取当前进程 id
print(os.getpid())
# 启动一个子进程 返回父进程 id 和子进程 id
pid = os.fork()
