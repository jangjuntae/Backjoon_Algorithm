T = input()
stack = []
stack_num = []
a = ''

for i in range(97, 123):
    stack.append(chr(i))

for i in range(97, 123):
    stack_num.append(0)

for i in range(26):
    for j in T:
        if stack[i] == j:
            stack_num[i] = stack_num[i] + 1

for i in range(26):
    a = a + str(stack_num[i])
    if i < 25:
        a = a + ' '

print(a)