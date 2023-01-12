import sys

n, m = map(int, sys.stdin.readline().split())
value = []
count = 1
value_sum = 0
cnt = 0
num = 0

while cnt < 1000:
    for j in range(count):
        value.append(count)
        cnt += 1
    count += 1

for i in range(n-1, m):
    value_sum += value[i]

print(value_sum)