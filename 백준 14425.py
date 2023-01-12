import sys

n, m = map(int, sys.stdin.readline().split())
key = []
count = 0

for i in range(n):
    key.append(sys.stdin.readline().strip())

for i in range(m):
    word = sys.stdin.readline().strip()
    if word in key:
        count += 1

print(count)