# !/usr/local/bin/python3


import time


def mystery(n):
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            sum += i
    return sum


def mystery_improve(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i**2
    return sum


def mystery_improve_improve(n):
    # sum = 0
    res = n * (n + 1) * (2 * n + 1) / 6
    return res


start = time.time()
a = mystery(100)
end = time.time()

print("sum = ", a, "time: ", end - start)

start2 = time.time()
a = mystery_improve(100)
end2 = time.time()
print("sum = ", a, "time: ", end2 - start2)
print((end2 - start2) - (end - start))
