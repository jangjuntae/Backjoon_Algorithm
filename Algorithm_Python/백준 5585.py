n = int(input())

n = 1000 - n

stack = [500, 100, 50, 10, 5, 1]

a = 0

for i in range(6):
    if n < stack[i]:
        continue
    if n == 0:
        break
    b = n // stack[i]
    n = n % stack[i]
    a += b