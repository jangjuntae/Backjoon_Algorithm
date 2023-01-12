from collections import deque
import sys

n = int(sys.stdin.readline())
time = []
count = 1

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    time.append([x, y])

time.sort(key=lambda x: (x[1], x[0]))
a = time[0][1]

for i in range(1, n):
    if a <= time[i][0]:
        a = time[i][1]
        count += 1

print(count)