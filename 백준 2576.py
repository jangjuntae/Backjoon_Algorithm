import sys

stack = []

for i in range(7):
    a = int(sys.stdin.readline())
    if a % 2 != 0:
        stack.append(a)


if len(stack) != 0:
    print(sum(stack))
    print(min(stack))
else:
    print(-1)