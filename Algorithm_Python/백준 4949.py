while True:
    sentence = input()
    if sentence == '.':
        break
    stack = []
    for i in sentence:
        if i == '(' or i == ')' or i == '[' or i == ']':
            stack.append(i)
        if len(stack) >= 2:
            if stack[-1] == ')' and stack[-2] == '(':
                stack.pop()
                stack.pop()
            elif stack[-1] == ']' and stack[-2] == '[':
                stack.pop()
                stack.pop()
        if i == '.':
            if stack:
                print('no')
                break
            else:
                print('yes')
                break