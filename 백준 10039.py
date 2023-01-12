def solution(list_avg):
    for i in range(len(list_avg)):
        if list_avg[i] < 40:
            list_avg[i] = 40
    return int(sum(list_avg) / len(list_avg))

stack = []
for i in range(5):
    stack.append(int(input()))

print(solution(stack))