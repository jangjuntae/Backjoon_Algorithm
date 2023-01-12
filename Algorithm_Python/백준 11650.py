import sys
n = int(sys.stdin.readline())

stack = []

for i in range(n):
    stack.append(list(map(int, sys.stdin.readline().split())))

stack.sort()

for i in range(n):
    print(stack[i][0], stack[i][1])

