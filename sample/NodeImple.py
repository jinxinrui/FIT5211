# !/usr/local/bin/python3


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


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

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

    def insert(self, pos, item):
        current = self.head
        temp = Node(item)
        previous = None
        curpos = 0
        if pos > self.size() or pos < 0:
            return -1
        while curpos != pos:
            curpos += 1
            previous = current
            current = current.getNext()
        if pos == 0:
            self.add(item)
        else:
            temp.setNext(current)
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
                self.head = None
                # return current
            else:
                previous.setNext(current.getNext())
            return current

    # def pop(self, pos=None):
    #     if self.size() == 0:
    #         return -1
    #     elif pos is None:
    #         (self.size() - 1)
    #     else:
    #         current = self.head
    #         current = current.getNext()
    #         previous = None
    #         curpos = 0
    #         while curpos != pos:
    #             previous = current
    #             current = current.getNext()
    #             curpos += 1
    #         previous.setNext(current.getNext())
    #
    #


mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.append(100)
# mylist.insert(1, 99)
print(mylist.index(100))
mylist.pop()
print(mylist.index(100))
print(mylist.index(93))
mylist.pop(2)
print(mylist.index(93))

print(mylist.size())
print(mylist.search(99))
# mylist.pop()
print(mylist.search(99))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))
