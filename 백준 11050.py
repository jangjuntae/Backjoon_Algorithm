import sys

n, m = map(int, sys.stdin.readline().split())
num = 1

for i in range(1, n+1):
    num *= i

for i in range(1, m+1):
    num //= i

for i in range(1, (n-m) + 1):
    num //= i

print(num)