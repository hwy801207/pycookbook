'''利用生成器实现迭代器'''
class MyContainer(object):
    def __init__(self):
        self.str = "hello world"
        self.its = [1,2, 3, 4]
        self.f = open('test.txt')

    def __iter__(self):
        for i in self.its:
            yield i
        for line in self.f:
            yield line


if __name__ == '__main__':
    mc = MyContainer() 
    for i in mc:
        print(i)
