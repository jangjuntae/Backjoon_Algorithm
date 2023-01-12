n, k = map(int, input().split())

stack = list()

for _ in range(n):
    stack.append(int(input()))

a = 0

while True:
    b = k // stack[n-1]

    a += b

    k = k % stack[n-1]

    if k == 0:
        break

    n -= 1

print(a)