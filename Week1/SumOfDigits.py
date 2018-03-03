# !/usr/local/bin/python3


def sum_digit_compute(n):
    sum = 0
    while True:
        sum += n % 10
        n = n // 10
        if n == 0:
            break
    return sum


def sum_digit_improve(n):
    n = sum_digit_compute(n)
    while (n // 10) > 0:
        n = sum_digit_compute(n)
    return n


a = sum_digit_improve(979853562951413)
print(a)
