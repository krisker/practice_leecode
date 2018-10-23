# 斐波那契数列的实现


#一，生成器方式的实现
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for index, x in enumerate(fib()):
    if index == 10:
        break
    print("%s"%(x))


#二， 迭代器方式的实现





#递归方式实现
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


