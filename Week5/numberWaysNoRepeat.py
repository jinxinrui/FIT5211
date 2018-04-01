# !/usr/local/bin/python3


# def numberOfWays(n):
#     a = [0] * (n + 1)
#     a[0] = 0
#     for i in range(1, n + 1):
#         a[i] = (i - 1) // 2
#     calls = 1 + a[n]
#     for j in range(n - 1, 0, -1):
#         if a[j] < n - j:
#             break
#         for k in range(j, 0, -1):
#
#         calls += a[j] - (n - j)
#         # print(calls)
#     return calls


def numberOfWays(n):
    mem = [[0] * (n + 1) for i in range(n + 1)]
    mem[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            for k in range(j):
                mem[i][j] += mem[i - j][k]
    res = 0
    for j in range(1, n + 1):
        res += mem[n][j]
    return res


def numberOfWaysImproven2(n):
    mem = [[0] * (n + 1) for i in range(n + 1)]
    mem[0][0] = 1
    mem[1][1] = 1
    mem[1][0] = 0
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            mem[i][j] = mem[i - 1][j - 1] + mem[i - j][j - 1]
    res = 0
    for j in range(1, n + 1):
        res += mem[n][j]
    return res


numberOfWays(15)
numberOfWaysImproven2(15)
