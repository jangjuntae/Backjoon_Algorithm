import sys

n = int(sys.stdin.readline())
name = {}

for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())

    if b == "enter":
        name[a] = "enter"
    else:
        if name[a]:
            del name[a]

name = sorted(name.keys(), reverse=True)

for i in name:
    print(i)