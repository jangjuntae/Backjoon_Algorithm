import sys

value_sum = []

for i in range(5):
    value_sum.append(int(sys.stdin.readline()))

print(sum(value_sum))