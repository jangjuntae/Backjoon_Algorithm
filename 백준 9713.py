import sys

n = int(sys.stdin.readline())

for i in range(n):
    value = 0
    count = 1
    num = int(sys.stdin.readline())
    while num >= count:
        if count % 2 == 1:
            value += count
        count += 1
    print(value)