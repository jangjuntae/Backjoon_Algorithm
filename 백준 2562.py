a_list = []

for i in range(9):
    a = int(input())
    a_list.append(a)

b = a_list[0]
c = 1
for i in range(9):
    if b < a_list[i]:
        b = a_list[i]
        c = i + 1

print(b)
print(c)