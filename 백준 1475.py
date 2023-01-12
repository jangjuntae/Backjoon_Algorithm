import sys
import math

n = list(map(int, sys.stdin.readline().rstrip()))
num_list = []

for i in range(10):
    num_list.append(n.count(i))

num_list[9] = math.ceil((num_list[9] + num_list[6]) / 2)

num_list[6] = 0

print(max(num_list))