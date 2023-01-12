import sys

n, m = map(int, sys.stdin.readline().split())
key = set()
value = set()

key.update(map(int, sys.stdin.readline().split()))
value.update(map(int, sys.stdin.readline().split()))

result_1 = list(key - value)
result_2 = list(value - key)

print(len(result_1) + len(result_2))