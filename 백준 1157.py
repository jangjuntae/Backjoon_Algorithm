a_String = str(input()).upper()

b_String = list(set(a_String))

cnt_list = []

for i in b_String:
    cnt = a_String.count(i)
    cnt_list.append(cnt)

if(cnt_list.count(max(cnt_list))) > 1:
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(b_String[max_index])