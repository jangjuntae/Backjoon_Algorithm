from collections import deque
import sys

n = int(sys.stdin.readline())
value = []

for i in range(n):
    value.append(list(map(int, sys.stdin.readline().split())))

value.sort()
value.sort(key=lambda x: x[1])

for i in range(n):
    print(value[i][0], value[i][1])
