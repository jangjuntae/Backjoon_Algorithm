import sys

n, m = map(int, sys.stdin.readline().split())
key = set()
value = set()

key.update(map(int, sys.stdin.readline().split()))
value.update(map(int, sys.stdin.readline().split()))

result = sorted(list(key - (key & value)))

print(len(result))

if len(result) != 0:
    for i in result:
        print(i, end = ' ')