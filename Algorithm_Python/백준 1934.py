def solution(x, y):
    if y == 0:
        return x
    else:
        return solution(y, x % y)

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(int(a * b / solution(a, b)))