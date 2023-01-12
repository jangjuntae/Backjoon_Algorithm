n = int(input())

L = list(map(int, input().split()))

L.sort(reverse = True)

result = 0
for i in range(1, n):
    b = L[0] + L[i]
    result += b

print(result)