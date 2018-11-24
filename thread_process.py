from multiprocessing import Process, current_process
import time
import os


def task(x):
    print("%s is running" % x)
    time.sleep(3)
    print("%s is done" % x)


if __name__ == '__main__':
    p1 = Process(target=task, args=("守护进程",))
    print(current_process)
    p2 = Process(target=task, args=("zi进程",))
    print(current_process)

    # p1.daemon = True
    p1.start()
    p2.start()
    print("主进程是%s" % current_process)


