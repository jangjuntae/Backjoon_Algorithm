a = int(input())
i = 0
k = a
while True:
    b, c = k // 10, k % 10
    k = (c*10) + (b + c) % 10
    i += 1

    if a == k:
        print(i)
        break