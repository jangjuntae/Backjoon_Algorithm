import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    max_value = 0
    stack = deque()
    n = int(sys.stdin.readline())
    tong = list(map(int, sys.stdin.readline().split()))
    tong.sort()
    tong = deque(tong)

    for i in range(len(tong)):
        if i % 2 == 0:
            stack.appendleft(tong.pop())
        else:
            stack.append(tong.pop())

    num = stack[0]

    for i in range(1, len(stack)):
        if max_value < abs(stack[i] - num):
            max_value = abs(stack[i] - num)
        num = stack[i]

    print(max_value)