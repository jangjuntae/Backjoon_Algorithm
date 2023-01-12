n = int(input())

stack = list(map(int, input().split()))

stack.sort()
result = 0
count = 0

for i in range(n):
    count += stack[i]
    result += count

print(result)