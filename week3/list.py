# !/usr/local/bin/python3


class Node:
    def __init__(self, initdata):
        self.Item = initdata
        self.next = None

    def getData(self):
        return self.Item

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.Item = newdata

    def setNext(self, newnext):
        self.next = newnext

    def size(self):
        if self.getNext() is None:
            return 1
        else:
            return 1 + self.getNext().size()

    def search(self, item):
        if self.getNext() is None:
            return False
        elif self.getData() == item:
            return True
        else:
            return self.getNext().search(item)
