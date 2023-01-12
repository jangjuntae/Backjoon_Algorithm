import sys
n = int(sys.stdin.readline())

num = [0] * 10000

for i in range(n):
    a = int(sys.stdin.readline())
    num[a - 1] += 1

for i in range(10000):
    if num[i] != 0:
        for _ in range(num[i]):
            print(i+1)
