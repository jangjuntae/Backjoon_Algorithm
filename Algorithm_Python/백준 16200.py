import sys

n = int(sys.stdin.readline())
stack = list(map(int, sys.stdin.readline().split()))
count = 0

stack.sort(reverse = True)


while len(stack) != 0:
    for i in range(stack[len(stack) - 1]):
        if len(stack) == 0:
            break
        stack.pop()
    count += 1

print(count)