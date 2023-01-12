T = int(input())

for i in range(T):
    stack = []
    a = list(input())
    for j in a:
        stack.append(j)
        if len(stack) >= 2:
            if stack[-1] == ')' and stack[-2] == '(':
                stack.pop()
                stack.pop()
    if stack:
        print('NO')
    else:
        print('YES')