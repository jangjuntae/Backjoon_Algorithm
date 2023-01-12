from collections import deque
import sys

while True:
    n, a, b = map(int, sys.stdin.readline().split())
    if n == 0 and a == 0 and b == 0:
        break

    num_list = []

    for i in range(n):
        num_list.append(list(map(int, sys.stdin.readline().split())))

    num_list.sort(key=lambda x: abs(x[1] - x[2]), reverse=True)
    result = 0

    for i in range(n):
        count = 0
        if num_list[i][1] <= num_list[i][2]:
            count = min(num_list[i][0], a)
        elif num_list[i][1] > num_list[i][2]:
            count = num_list[i][0] - min(num_list[i][0], b)

        result += (num_list[i][1] * count) + (num_list[i][2] * (num_list[i][0] - count))
        a -= count
        b -= num_list[i][0] - count

    print(result)