import sys

stack_1 = []
stack_2 = []
value = 0

for i in range(4):
    stack_1.append(int(sys.stdin.readline()))

for i in range(2):
    stack_2.append(int(sys.stdin.readline()))

stack_1.sort()
stack_2.sort()

for i in range(1, 4):
    value += stack_1[i]

value += stack_2[1]

print(value)