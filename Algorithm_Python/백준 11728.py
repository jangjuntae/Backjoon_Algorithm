import sys
n, m = map(int, sys.stdin.readline().split())

num = list((map(int, sys.stdin.readline().split())))

num_2 = list((map(int, sys.stdin.readline().split())))

for i in range(len(num_2)):
    num.append(num_2[i])

num.sort()

for i in range(len(num)):
    print(num[i], end = ' ')
