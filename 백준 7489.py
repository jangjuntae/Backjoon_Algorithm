import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    value = 1
    if n != 1:
        for j in range(2, n+1):
            value *= j
    for k in reversed(range(len(str(value)))):
        if str(value)[k] != '0':
            print(str(value)[k])
            break