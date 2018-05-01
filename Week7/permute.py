# !/usr/local/bin/python3


def permute(l, p):
    assert(len(l) == len(p))
    pofl = [None] * len(l)
    for i in range(0, len(l)):
        pofl[i] = l[p[i]]
    return pofl


l = ["a", "b", "c", "d"]
p = [2, 0, 3, 1]

permute(l, p)
