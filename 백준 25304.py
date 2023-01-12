import sys

price = int(sys.stdin.readline())
n = int(sys.stdin.readline())
result = 0

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    result += a*b

if price == result:
    print('Yes')
else:
    print('No')