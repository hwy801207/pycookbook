#!/usr/bin/env python3
"""
实现一个优先级队列
本质是元组列表中，元组是如何比较大小的
本例子中index的使用也挺讲究的
"""
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('zoo'), 5)
    q.push(Item('bar'), 4)
    q.push(Item('zoor'), 3)
    q.push(Item('ping'), 3)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
