import sys
n, k = map(int, sys.stdin.readline().split())

result = list(map(int, sys.stdin.readline().split()))

result.sort(reverse = True)

print(result[k - 1])
