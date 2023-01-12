import sys

x = int(sys.stdin.readline())
count = 1

for _ in range(x):
    stack = list(map(int, sys.stdin.readline().split()))
    stack.remove(stack[0])
    stack.sort()
    a = stack[0]
    gap = []
    for i in range(1, len(stack)):
        gap.append(stack[i] - a)
        a = stack[i]
    print("Class %d" %(count))
    print("Max %d, Min %d, Largest gap %d" %(max(stack), min(stack), max(gap)))
    count += 1


