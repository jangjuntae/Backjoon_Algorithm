import sys

x, y, z = map(int, sys.stdin.readline().split())

result = (x * y) - z

if result > 0:
    print(result)
else:
    print(0)