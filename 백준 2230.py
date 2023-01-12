from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
num = []
left = 0
right = 1
min_value = 10**15

for i in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

while left < n and right < n:
    if num[right] - num[left] == m:
        min_value = m
        print(min_value)
        exit(0)
    elif num[right] - num[left] < m:
        right += 1
        continue
    elif num[right] - num[left] >= m:
        min_value = min(min_value, num[right] - num[left])
        left += 1

print(min_value)