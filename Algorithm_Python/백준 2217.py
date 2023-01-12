n = int(input())

stack = []

for _ in range(n):
    stack.append(int(input()))

stack.sort()
result = []

for i in stack:
    result.append(n*i)
    n -= 1
print(max(result))