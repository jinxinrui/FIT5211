# !/usr/local/bin/python3


def ways(n, mem=None):
    calls = 1
    if mem is None:
        mem = [0] * (n + 1)
    # if mem[n] is not None:
    #     return mem[n]
    mem[0] = 1
    for i in range(1, n):
        for j in range(i):
            mem[i] += mem[j]
        calls += mem[i]
    return calls


# def waysImprove(n, mem=None):
#     calls = 1
#     if mem is None:
#         mem = [None] * (n + 1)
#     mem[n] = 1
#     mem[0] = 1
#     for i in range(1, n):


ways(4)
