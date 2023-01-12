import sys
n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

num = list(set(num))
num.sort()

for i in range(len(num)):
    print(num[i], end = ' ')
