S = input()
stack = []
num = 0
for i in range(len(S)):
    stack.append(S[num:])
    num = num + 1
stack.sort()
for i in range(len(stack)):
    print(stack[i])