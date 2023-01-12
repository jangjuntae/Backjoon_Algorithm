import sys

number = list(map(int, sys.stdin.readline().split()))
chess = [1, 1, 2, 2, 2, 8]
result = [0] * 6

for i in range(len(number)):
    result[i] = chess[i] - number[i]

for i in range(len(result)):
    print(result[i], end=' ')