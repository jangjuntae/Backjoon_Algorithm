import sys

value_dic = {'0':"zero", '1':"one", '2':"two", '3':"three", '4':"four", '5':"five", '6':"six", '7':"seven", '8':"eight", '9':"nine"}

n, m = map(int, sys.stdin.readline().split())
value = []
count = 0

for i in range(n, m+1):
    num = str(i)
    word = ''
    for j in range(len(num)):
        word += value_dic[num[j]]
    value.append((i, word))

value.sort(key=lambda x: x[1])
for i in range(len(value)):
    count += 1
    print(value[i][0], end = ' ')
    if count % 10 == 0:
        print()