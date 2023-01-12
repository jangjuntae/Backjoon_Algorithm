import sys

max_value = 0
num = 0

for i in range(4):
    a, b = map(int, sys.stdin.readline().split())
    num -= a
    num += b
    max_value = max(max_value, num)

print(max_value)