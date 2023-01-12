n = int(input())

stack = [300, 60, 10]
result = []

for i in range(3):
    result.append(n // stack[i])
    n = n % stack[i]

if n == 0:
    print(result[0], result[1], result[2])
else:
    print("-1")