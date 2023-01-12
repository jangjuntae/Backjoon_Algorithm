import sys

n = int(sys.stdin.readline())
count = 1
result = 0

while n != 0:
    if count > n:
        count = 1
    n = n - count
    count += 1
    result += 1