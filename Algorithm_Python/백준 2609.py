def solution_max(a, b):
    stack_a = []
    stack_b = []
    stack_max = []
    for i in range(1, a + 1):
        if a % i == 0:
            stack_a.append(i)
    for i in range(1, b + 1):
        if b % i == 0:
            stack_b.append(i)
    for i in range(len(stack_a)):
        for j in range(len(stack_b)):
            if stack_a[i] == stack_b[j]:
                stack_max.append(stack_a[i])
    return max(stack_max)


def solution_min(a, b):
    c = a
    d = b
    while a != b:
        if a > b:
            b = b + d
        elif a < b:
            a = a + c
        else:
            break
    return a


a, b = map(int, input().split())
print(solution_max(a, b))
print(solution_min(a, b))