num = 0

for i in range(4):
    a = input()
    b = input()
    count = 0
    for j in range(8):
        if count % 2 == 0 and a[j] != '.':
            num = num + 1
        if count % 2 != 0 and b[j] != '.':
            num = num + 1
        count = count + 1
print(num)