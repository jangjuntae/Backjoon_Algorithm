N = int(input())
num = N

for i in range(N):
    word = list(str(input()))
    for j in range(len(word) - 1):
        if word[j] != word[j+1]:
            if word[j] in word[j+1:]:
                num = num - 1
                break

print(num)