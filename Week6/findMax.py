# !/usr/local/bin/python3


from Week6.hashtable import *


def findMax(H, up):
    for i in range(up, H.size - 1, -1):
        if search(H, i):
            return i


H = HashTable()
H[50] = 50
findMax(H, 54)
