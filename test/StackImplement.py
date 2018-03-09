# !/usr/local/bin/python3

from pythonds.basic.stack import Stack


def revstring(revstr=""):
    alist = Stack()
    blist = ''
    for ch in revstr:
        alist.push(ch)
    while not alist.isEmpty():
        blist += alist.pop()
    return blist


print(revstring("Happy"))
