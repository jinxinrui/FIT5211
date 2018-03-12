# !/usr/local/bin/python3


def iterateBis(x, e):
    level = 10
    sqr = 0
    for i in range(e + 1):
        level *= 0.1
        for j in range(10):
            j = level * j + sqr
            if j * j <= x:
                temp = j
            else:
                break
        sqr = temp
    return sqr


def recursiveBis(x, e):
    if e == 0:
        for i in range(10):
            if i * i <= x:
                temp = i
            else:
                break
        return temp
    else:
        res = recursiveBis(x, e - 1)
        for i in range(10):
            i = i * (0.1 ** e)
            if ((i + res) ** 2) <= x:
                temp = i
            else:
                break
        return (temp + res)


iterateBis(2, 20)
print(0.1 ** 5)
recursiveBis(2, 20)
