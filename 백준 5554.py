from collections import deque
import sys
sys.setrecursionlimit(10**6)

result = 0

for i in range(4):
    second = int(sys.stdin.readline())
    result += second

print(result // 60)
print(result % 60)