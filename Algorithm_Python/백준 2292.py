N = int(input())

count = 0
bee = 1
while N > bee:
    if N == 1:
        count = 1
        break
    bee = bee + count * 6
    count += 1

if count == 0:
    count += 1

print(count)