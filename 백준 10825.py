from collections import deque
import sys

n = int(sys.stdin.readline())
subject = []

for _ in range(n):
    subject.append(list(sys.stdin.readline().split()))

subject.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(subject[i][0])