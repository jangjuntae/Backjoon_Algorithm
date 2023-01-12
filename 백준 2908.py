a, b = map(int, input().split())

c = ""
d = ""

a_list = list(str(a))
a_list.reverse()
for i in a_list:
    c = c + i

b_list = list(str(b))
b_list.reverse()
for i in b_list:
    d = d + i

int(c)
int(d)

if c > d:
    print(c)
else:
    print(d)