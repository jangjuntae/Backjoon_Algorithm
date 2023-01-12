import sys

n = int(sys.stdin.readline())
result = []

for i in range(n):
    result.append(sys.stdin.readline().strip())

result = list(set(result))
result.sort()
result.sort(key=lambda x: len(x))

for i in range(len(result)):
    print(result[i])