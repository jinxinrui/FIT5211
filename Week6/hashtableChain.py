# !/usr/local/bin/python3


def genKey(s):
    res = 0
    mod = 1000000009
    for i in s:
        res = (res * 26 + (ord(i) - ord('a'))) % mod
    return res % mod


class HashTable:
    def __init__(self):
        self.size = 50
        self.slots = [[] for i in range(self.size)]
        self.data = [[] for i in range(self.size)]

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))
        self.slots[hashvalue].append(key)
        self.data[hashvalue].append(data)

    def hashfunction(self, key, size):
        return key % size

    # def rehash(self, oldhash, size, location):
    #     return (oldhash + location) % size

    def get(self, key):
        slot = self.hashfunction(key, len(self.slots))

        data = None
        # stop = False
        found = False
        position = 0
        while len(self.slots[slot]) > position and  \
                not found:
            if self.slots[slot][position] == key:
                found = True
                data = self.data[slot][position]
            else:
                position = position + 1
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


def search(table, item):
    key = genKey(item)
    if table[key] is not None:
        return True
    else:
        return False


H = HashTable()
H[genKey("cat")] = "cat"
H[genKey("dog")] = "dog"
H[genKey("lion")] = "lion"
H[genKey("tiger")] = "tiger"
H[genKey("bird")] = "bird"
H[genKey("cow")] = "cow"
H[genKey("goat")] = "goat"
H[genKey("pig")] = "pig"
H[genKey("chicken")] = "chicken"

search(H, "dot")
genKey("lion")
print(H.slots)
print(H.data)
H[genKey("lion")]
