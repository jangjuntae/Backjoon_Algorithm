import sys

n, m = map(int, sys.stdin.readline().split())

gugu_dan = []

for j in range(1, m + 1):
    gugu_dan.append(int(str(n*j)[::-1]))

print(max(gugu_dan))