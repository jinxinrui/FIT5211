
def pow(x, n):
    """
        every n can be a binary number
        so x^n = x^(2^k1)*x^(2^k2)*x^(2^k3)....
    """
    res = 1
    while n > 0:
        # n can be a binary number and the first
        # number of the n will show whether its odd
        # or even
        if n & 1:
            res *= x
        x *= x  # ex: 2^0=>2^1, 2^1=>2^2
        n >>= 1  # ex: 1111 => 111
    return res


# n = 6
# n >>= 1
# print(n & 1)

# print(3 & 1)
pow(2, 5)
