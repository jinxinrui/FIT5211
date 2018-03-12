# !/usr/local/bin/python3
import random

a = random.Random(15, 45)


class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value


class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class PriorityQueue:

    def __init__(self):
        self.head = None

    def printListElement(self):
        current = self.head
        while current is not None:
            print(str(current.data.getKey()) +
                  " " + str(current.data.getValue()))
            current = current.getNext()

    def isEmpty(self):
        return self.head is None

    def insert(self, key, value):
        temp = Node(Item(key, value))
        temp.setNext(self.head)
        self.head = temp

    def insertOrder(self, key, value):
        current = self.head
        temp = Node(Item(key, value))
        previous = None
        if current is None:
            self.insert(key, value)
        else:
            while True:
                if current.data.getKey() == key:
                    return -1
                elif current.data.getKey() < key:
                    previous = current
                    current = current.getNext()
                    if current is None:
                        break
                else:
                    break
            temp.setNext(current)
            if previous is None:
                self.head = temp
            else:
                previous.setNext(temp)

    def delMin(self):
        current = self.head
        # previous = None
        curKey = 10000
        Loc = 0
        remLoc = 0
        while current is not None:
            if curKey >= current.data.getKey():
                curKey = current.data.getKey()
                current = current.getNext()
                remLoc = Loc
            else:
                current = current.getNext()
            Loc += 1
        return self.pop(remLoc)

    def delMinOrder(self):
        # current = self.head
        # self.head = current.getNext()
        # return current
        return self.pop(0)

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        found = False
        current = self.head
        while (current is not None) and (not found):
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found and current is not None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        previous = None
        current = self.head
        temp = Node(item)
        while current is not None:
            previous = current
            current = current.getNext()
        if previous is None:
            self.add(item)
        else:
            previous.setNext(temp)

    def index(self, item):
        if self.size() == 0:
            return -1
        else:
            current = self.head
            # current = current.getNext()
            itemindex = 0
            while current is not None:
                if current.getData() == item:
                    return itemindex
                else:
                    current = current.getNext()
                    itemindex += 1
            return -1

    def pop(self, pos=None):
        # if pos is None:
        if self.head is None:
            return -1
        elif pos is None:
            self.pop(self.size() - 1)
        else:
            current = self.head
            previous = None
            curpos = 0
            while curpos < pos:
                # while (current.getNext() is not None) and (curpos < pos):
                previous = current
                current = current.getNext()
                curpos += 1
            if previous is None:
                self.head = current.getNext()
                # return current
            else:
                previous.setNext(current.getNext())
            return current


Mylist = PriorityQueue()
Mylist.insert(1, "abc")
Mylist.insert(2, "bac")
Mylist.printListElement()
Mylist.size()
Mylist.delMin().data.getValue()
Mylist.delMin().data.getValue()

MyList2 = PriorityQueue()
MyList2.insertOrder(1, "abc")
MyList2.printListElement()
MyList2.insertOrder(3, "bac")
MyList2.printListElement()
MyList2.insertOrder(2, "aaa")
MyList2.printListElement()
MyList2.delMinOrder().data.getValue()
MyList2.printListElement()
MyList2.size()
