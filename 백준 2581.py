m = int(input())
n = int(input())

sosu_list = []
for i in range(m, n + 1):
    stack = []
    for j in range(1, i + 1):
        if i % j == 0:
            stack.append(j)
            if len(stack) > 2:
                break
    if len(stack) == 2:
        sosu_list.append(i)

if len(sosu_list) != 0:
    sosu_sum = sum(sosu_list)
    sosu_min = min(sosu_list)

if len(sosu_list) == 0:
    print(-1)
else:
    print(sosu_sum)
    print(sosu_min)