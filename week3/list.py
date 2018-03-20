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

    def isDecreasing(self, previousitem=None):
        if previousitem is not None and self.getData() > previousitem:
            return False
        elif self.getNext() is None:
            return True
        else:
            return self.getNext().isDecreasing(self.getData())


class UnorderedListWithRecursion(unorderedList):
    def size(self):
        if self.head is None:
            return 0
        else:
            return self.head.size()

    def search(self, item):
        if self.head is None:
            return False
        else:
            return self.head.search(item)

    def isDecreasing(self, previousitem=None):
        if self.head is None:
            return False
        else:
            return self.head.isDecreasing()
