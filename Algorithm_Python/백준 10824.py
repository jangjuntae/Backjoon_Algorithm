import sys

a, b, c, d = map(int, sys.stdin.readline().split())

num_1 = str(a) + str(b)
num_2 = str(c) + str(d)

print(int(num_1) + int(num_2))