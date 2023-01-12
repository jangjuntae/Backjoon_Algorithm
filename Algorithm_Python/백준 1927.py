import sys
import heapq
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    a = int(input())
    if a == 0:
        if len(stack) == 0:
            print(0)
            continue
        print(heapq.heappop(stack))
    else:
        heapq.heappush(stack, a)