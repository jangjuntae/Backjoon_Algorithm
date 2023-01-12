a = int(input())
count = 1
count_1 = 0

for i in range(a):
    o_list = list(str(input()))
    o_list.append(" ")
    for j in range(0, len(o_list)):
        if o_list[j] == 'O':
            count_1 = count_1 + count
            if o_list[j+1] == 'O':
                count = count + 1
            # print(count_1)
            # print(count)
            else:
                count = 1
    print(count_1)
    count = 1
    count_1 = 0