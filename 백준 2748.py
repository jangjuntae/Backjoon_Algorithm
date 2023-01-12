n = int(input())
stack = []
for i in range(n):
    if i < 2:
        stack.append(1)
    else:
        stack.append(stack[i-1] + stack[i-2])
print(stack[n-1])