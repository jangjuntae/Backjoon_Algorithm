import sys
from collections import deque

n = int(sys.stdin.readline())
value = []

for i in range(31):
    value.append(2**i)

if n in value:
    print(1)
else:
    print(0)