import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
value_sum = 0
num = 1
value = 0
stack = []
max_value = []

while value < 10000:
    value = num * num
    stack.append(value)
    num += 1

for i in range(n, m+1):
    if i in stack:
        max_value.append(i)

if len(max_value) != 0:
    print(sum(max_value))
    print(max_value[0])
else:
    print(-1)