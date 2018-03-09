# !/usr/local/bin/python3

from pythonds.basic.stack import Stack


class Queue:
    def __init__(self):
        # self.items = []
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, item):
        self.inbox.push(item)

    def dequeue(self):
        assert(self.outbox.isEmpty())
        while not self.inbox.isEmpty():
            self.outbox.push(self.inbox.pop())
        res = self.outbox.pop()
        while not self.outbox.isEmpty():
            self.inbox.push(self.outbox.pop())
        return res

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self.inbox.size()


testQueue = Queue()
testQueue.enqueue("abc")
testQueue.enqueue("def")
testQueue.enqueue("ghj")
testQueue.dequeue()
testQueue.dequeue()
testQueue.size()
