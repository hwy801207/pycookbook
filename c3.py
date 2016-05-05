#!/usr/bin/env python3
'''
保留最后N个元素
'''
from collections import deque

'''
这里实际是个迭代器, 实现了搜索与搜索结果的分离，非常的漂亮
deque的特性也用在很多地方
'''
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open("somefile.txt") as f:
        #这里其实才是搜索的结果的使用
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print("line ",line, end="")
            print('-'*20)

"""
deque的使用
"""
q = deque(maxlen=5)
#可插入各种类型的数据
q.append(5)
q.append("str")
q.append([1,2,3,4])
# pop
s = q.pop()
#s的值是[1,2,3,4]
print(s)

#remove 移除第一个匹配的, 但是如果没有就会报ValueError异常
s.remove(5)

#clear 清理deque里的数据，但是deque本身的属性并没发生变化
s.clear()
