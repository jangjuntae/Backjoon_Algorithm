import sys

n, m = map(int, sys.stdin.readline().split())
key = set()
value = set()

for i in range(n):
    key.add(sys.stdin.readline().strip())

for i in range(m):
    value.add(sys.stdin.readline().strip())

result = sorted(list(key & value))

print(len(result))
for i in result:
    print(i)