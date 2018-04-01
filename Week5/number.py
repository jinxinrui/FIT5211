# !/usr/local/bin/python3


def f(n):
    mem = [1] * (n // 2 + 2)
    mem[0] = 0
    for i in range(n // 2 + 2):
        for j in range(2, i // 2 + 2):
            mem[i] += mem[j]
        if i % 2 == 0:
            mem[i] -= 1
    for j in range(2, n // 2 + 1):
        mem[i] += mem[j]
