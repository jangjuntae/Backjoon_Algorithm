import sys, copy

n = int(sys.stdin.readline())

num = [sys.stdin.readline().strip() for _ in range(n)]

num.sort(key=lambda x: float(x))

print(num[1])