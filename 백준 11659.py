import sys

n, m = map(int, sys.stdin.readline().split())
value = list(map(int, sys.stdin.readline().split()))
prefix_sum = [0] * (n+1)
sum_num = 0

for i in range(1, n + 1):
    sum_num = sum_num + value[i-1]
    prefix_sum[i] = sum_num

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(prefix_sum[b] - prefix_sum[a - 1])

