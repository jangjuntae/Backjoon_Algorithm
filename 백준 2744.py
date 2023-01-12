word = list(input())
stack = ''
for i in range(len(word)):
    if 65 <= ord(word[i]) <= 91:
        stack = stack + word[i].lower()
    if 97 <= ord(word[i]) <= 123:
        stack = stack + word[i].upper()

print(stack)