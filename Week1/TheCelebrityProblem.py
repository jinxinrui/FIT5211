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
        if not mat[i][c]:
            return -1
        if mat[c][i]:
            return -1
    return c


# def celebrity_improve(mat=[[]]):
#     n = len(mat)
#     check = [True for i in range(n)]
#     c = 0
#     for i in range(1,n):
#         if mat[c][i]:
#             check[c] = False


n = 10
check = [True for i in range(n)]
print(check)
print(type(check))
