# !/usr/local/bin/python3


def multi(x, y):
    if y == 0:
        return 0
    # elif y == 1:
    #     return x
    else:
        return x + multi(x, y - 1)


multi(5, 1)
