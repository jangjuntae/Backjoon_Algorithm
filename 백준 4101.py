import sys

while True:
    x, y = map(int, sys.stdin.readline().split())
    if x == 0 and y == 0:
        break
    if x > y:
        print('Yes')
    else:
        print('No')