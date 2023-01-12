import sys
n = int(sys.stdin.readline())

result = []

for i in range(n):
    result.append(int(sys.stdin.readline()))

result.sort(reverse = True)

for i in range(n):
    print(result[i])