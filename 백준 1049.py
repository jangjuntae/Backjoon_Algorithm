n, m = map(int, (input().split()))

stack = []
stack_1 = []
result = 0

for i in range(m):
    value = list(map(int, input().split()))
    stack.append(value[0])
    stack_1.append(value[1])

stack.sort()
stack_1.sort()

if n // 6 >= 1:
    if stack[0] < stack_1[0] * 6:
        result += stack[0] * (n//6)
    else:
        result += stack_1[0] * 6 * (n//6)
    if stack[0] < stack_1[0] * (n % 6):
        result += stack[0]
    else:
        result += stack_1[0] * (n % 6)
else:
    if stack[0] < stack_1[0] * (n % 6):
        result += stack[0]
    else:
        result += stack_1[0] * (n % 6)

print(result)