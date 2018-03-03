# !/usr/local/bin/python3


def celebrity(mat=[[]]):
    n = len(mat)
    check = [True for i in range(n)]
    c = 0
    for i in range(1, n):
        if mat[c][i]:
            check[c] = False
            c = i
        else:
            check[i] = False

    assert(check[c] == True)
    for i in range(n):
        if i == c:
            continue
        if not check[i][c]:
            return -1
        if check[c][i]:
            return -1
    return c
