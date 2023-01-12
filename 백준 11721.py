word = str(input())
a = ''

for i in range(len(word)):
    a = a + word[i]
    if (i + 1) % 10 == 0:
        a = a + '\n'
print(a)