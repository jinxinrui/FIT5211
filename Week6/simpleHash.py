# !/usr/local/bin/python3

import hashtable


def hash(str):
    return ord(str[0]) % 11
