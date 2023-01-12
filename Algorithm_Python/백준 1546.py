a = int(input())
b_list = list(map(int, input().split()))
avg_list = []

c = max(b_list)

for i in b_list:
    d = i/c*100
    avg_list.append(d)

e = 0
for i in avg_list:
    e = e + i

print(e/a)