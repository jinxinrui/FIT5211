
def pow(x, n):
    res = 1
    while n:
        if n & 1:
            res *= x
        else:
            x *= x
        n //= 2
    return res


print(3 & 1)
