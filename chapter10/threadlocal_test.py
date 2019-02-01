# -*- coding: utf-8 -*-
import threading

local_shcool = threading.local()  # 全局变量


# 通过 ThreadLocal 来获取线程的局部变量，防止线程代码传递参数的复杂
# 如果不使用 thread_local 需要不断的向下传递参数，thread_local 相当于一个全局的 dict
# 将线程作为 key 变量作为 value,可以直接通过线程获取变量，不用重复传递参数
def proces_student():
    # 获取当前线程关联的 student
    std = local_shcool.student
    print('thread %s process std', (threading.current_thread().name, std))


def thread_code(name):
    # 将 name 绑定到 thread_local
    local_shcool.student = name
    proces_student()


if __name__ == '__main__':
    # 线程1处理张三
    thread1 = threading.Thread(target=thread_code, name='thread1', args=('张三',))
    # 线程2处理李四
    thread2 = threading.Thread(target=thread_code, name='thread2', args=('李四',))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print('process end')
