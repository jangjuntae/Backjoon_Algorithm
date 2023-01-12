import sys

n, m = map(int, sys.stdin.readline().split(':'))


def solve(a, b):
    while b > 0:
        tmp = a
        a = b
        b = tmp % b
    return a


max_value = solve(n, m)
print("%d:%d" % (n // max_value, m // max_value))