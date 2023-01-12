from collections import deque
import sys
sys.setrecursionlimit(10**5)

n = int(sys.stdin.readline())
value = list(map(int, sys.stdin.readline().split()))
value.sort()

print(value[0]*value[n-1])