# !/usr/local/bin/python3
import re
from pythonds.basic.deque import Deque
from TestSuite import test


def palindrome(d):
    if d.size() <= 1:
        return True
    elif d.removeFront() != d.removeRear():
        return False
    else:
        return palindrome(d)


def convertDeque(s):
    d = Deque()
    gen = (i for i in s if re.match('[a-zA-Z]', i))
    for i in gen:
        d.addRear(i)
    return d


test(palindrome(convertDeque("ab ccba")) is True)
test(palindrome(convertDeque("ab'ccba")) is True)

print(" " in "abc")

b = ['c', 'b', 'c']
b.remove("c")
b = "".join(b)
print(b)
