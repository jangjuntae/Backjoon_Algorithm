n, L = map(int, input().split())

stack = list(map(int, input().split()))

stack.sort()

for i in range(n):
    if L >= stack[i]:
        L += 1
    else:
        break

print(L)

