num = list(input())
a = ''

num.sort()
num.reverse()
for i in range(len(num)):
    a = a + num[i]

print(a)