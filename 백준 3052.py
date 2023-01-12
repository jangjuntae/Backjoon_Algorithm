num_list = []

for i in range(10):
    a = int(input()) % 42
    num_list.append(a)

set_list = set(num_list)
print(len(set_list))