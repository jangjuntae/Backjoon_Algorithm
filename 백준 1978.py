def solution(s_list):
    sosu = []
    for i in s_list:
        stack = []
        for j in range(1, i + 1):
            if i % j == 0:
                stack.append(j)
            if len(stack) > 2:
                break
        if len(stack) == 2:
            sosu.append(i)
    return len(sosu)

n = int(input())
sosu_list = list(map(int, input().split()))

print(solution(sosu_list))