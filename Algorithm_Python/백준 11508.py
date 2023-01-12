n = int(input())

count = 0
result = 0
ksg = []
for _ in range(n):
    ksg.append(int(input()))

ksg.sort(reverse=True)

for i in range(n):
    count += 1
    if count == 3:
        result += 0
        count = 0
    else:
        result += ksg[i]

print(result)
