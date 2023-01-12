import sys

n, m, k = map(int, sys.stdin.readline().split())


def solution(a, b):
    if b == 0:
        return 1

    x = solution(a, b//2) % k

    if b % 2 == 0:
        return x * x
    else:
        return x * x * a


print(solution(n, m) % k)