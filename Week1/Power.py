
def pow(x, n):
    res = 1
    while n:
        if n & 1:
            res *= x
        x *= x
        n >>= 1
    return res


# n = 6
# n >>= 1
# print(n & 1)

# print(3 & 1)
pow(2, 5)
