import sys

n = int(sys.stdin.readline())
count = 0
for i in range(n, 0, -1):
    print((' '*count) + ('*'*i))
    count += 1