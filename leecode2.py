# 定义自己的range

class MyRange():
    def __init__(self, start, end=None, step=1):
        if end is None:
            self.end = start
            self.start = 0
        else:
            self.start = start
            self.end = end
        self.step = step

    #__iter__返回一个的是一个可迭代的对象
    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            result = self.start
            self.start += self.step
            return result
        raise StopIteration()

for i in MyRange(5):
    print(i)
    