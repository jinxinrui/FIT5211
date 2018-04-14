# !/usr/local/bin/python3


def genKey(s):
    res = 0
    mod = 1000000009
    for i in s:
        res = (res * 26 + (ord(i) - ord('a'))) % mod
    return res % mod


def search(table, item):
    if type(item) == "str":
        key = genKey(item)
    else:
        key = HashTable.hashfunction(item)
    if table[key] is not None:
        return True
    else:
        return False


class HashTable:
    def __init__(self):
        self.size = 50
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                i = 2
                nextslot = self.rehash(hashvalue, len(self.slots), 1)
                while self.slots[nextslot] is not None and \
                        self.slots[nextslot] != key:
                    nextslot = self.rehash(
                        nextslot, len(self.slots), 2 * i - 1)
                    i = i + 1

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size, location):
        return (oldhash + location) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] is not None and  \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


# H = HashTable()
# H[genKey("cat")] = "cat"
# H[genKey("dog")] = "dog"
# H[genKey("lion")] = "lion"
# H[genKey("tiger")] = "tiger"
# H[genKey("bird")] = "bird"
# H[genKey("cow")] = "cow"
# H[genKey("goat")] = "goat"
# H[genKey("pig")] = "pig"
# H[genKey("chicken")] = "chicken"
# H[genKey("chicken")] = "chicken"
