a = str(input())
b = 1

for i in range(len(a)):
    if a[i] == " ":
        b += 1

if a[0] == " ":
    b = b - 1

if a[len(a) - 1] == " ":
    b = b - 1

print(b)