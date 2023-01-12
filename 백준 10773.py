K = int(input())
stack = []

for i in range(K):
    a = input()
    if a == '0':
        stack.pop()
    else:
        stack.append(int(a))

print(sum(stack))