import sys
input =sys.stdin.readline

words=[list(map(str,input().rstrip())) for _ in range(5)]
lst=[[] for _ in range(15)]

for i in range(5):
    for j in range(len(words[i])):
        lst[j].append(words[i][j])

new_lst=[]
for c in lst:
    new_lst.append(''.join(c))

print(''.join(new_lst))