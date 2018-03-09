# !/usr/local/bin/python3


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


class PriorityQueueUnorder:
    def __init__(self):
        self.items = []

    def printAllElements(self):
        for i in range(self.size()):
            print(str(self.items[i].key) + " " + str(self.items[i].value))

    def insert(self, key, value):
        self.items.insert(0, Item(key, value))

    def delMin(self):
        minKey = self.items[0].getKey()
        loc = 0
        for i in range(1, self.size()):
            if self.items[i].getKey() < minKey:
                minKey = self.items[i].getKey()
                loc = i
        return self.items.pop(loc)

    def size(self):
        return len(self.items)


class PriorityQueueOrder:
    def __init__(self):
        self.items = []

    def printAllElements(self):
        for i in range(self.size()):
            print(str(self.items[i].key) + " " + str(self.items[i].value))

    def insert(self, key, value):
        if self.size() == 0:
            self.items.insert(0, Item(key, value))
        else:
            for i in range(self.size()):
                if self.items[i].getKey() > key:
                    self.items.insert(i, Item(key, value))
                    return True
                elif self.items[i].getKey() == key:
                    return False
            self.items.append(Item(key, value))
            return True

    def delMin(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


class SetADT:
    def __init__(self):
        self.items = []

    def printAllElements(self):
        for i in range(self.size()):
            print(str(self.items[i].key) + " " + str(self.items[i].value))

    def insert(self, key, value):
        valist = []
        for i in range(self.size()):
            valist.append(self.items[i].getValue())
        if value in valist:
            return False
        else:
            if self.size() == 0:
                self.items.insert(0, Item(key, value))
            else:
                for i in range(self.size()):
                    if self.items[i].getKey() > key:
                        self.items.insert(i, Item(key, value))
                        return True
                    elif self.items[i].getKey() == key:
                        return False
                self.items.append(Item(key, value))
                return True

    def size(self):
        return len(self.items)


# myList = PriorityQueueOrder()
# myList.insert(2, "123")
# myList.insert(1, "321")
# myList.size()
# myList.printAllElements()
# myList.delMin()
# myList.printAllElements()

mylist = SetADT()
mylist.insert(1, "123")
mylist.insert(2, "213")
mylist.insert(5, "512")
mylist.insert(4, "432")
mylist.insert(4, "444")
mylist.insert(3, "432")
mylist.printAllElements()
