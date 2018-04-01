# !/usr/local/bins/python3


def sumOfNumberWay(n, mem=None):
    sum = 1  # n = n
    if mem is None:
        mem = [None] * n
        mem[0] = 1
    if n == 1:
        return [mem[0], mem]
    elif mem[n - 1] is not None:
        # print("in this condition")
        return [mem[n - 1], mem]
    else:
        for i in range(1, n):
            sum = sum + sumOfNumberWay(i, mem)[0]
        mem[n - 1] = sum
        return [sum, mem]


print(sumOfNumberWay(4))
