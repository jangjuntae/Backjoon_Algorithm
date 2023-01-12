word = input()
stack = []
a = ''

for i in range(65, 91):
    stack.append(chr(i))

for i in word:
    for j in range(26):
        if i == stack[j]:
            a = a + i

print(a)