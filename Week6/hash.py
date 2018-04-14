# !/usr/local/bin/python3


def hash(s):
    """
    1. assume data are string
    2. assume string in lowercase
    3. regard string as on 26 based int
    4. map the big int to int in [0,mod)
    """
    res = 0
    mod = 1000000000
    for i in s:
        res = (res * 26 + (ord(i) - ord('a'))) % mod
    return res % mod
