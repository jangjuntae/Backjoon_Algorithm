c = int(input())

for i in range(c):
    a = 0
    avg_list = []
    n_list = list(map(int, input().split()))
    for j in range(1, len(n_list)):
        a = a + n_list[j]
    b = a / n_list[0]
    for k in range(1, len(n_list)):
        if n_list[k] > b:
            avg_list.append(n_list[k])
    num = round(len(avg_list) / (len(n_list) - 1) * 100, 3)
    print(str(f'{num:.3f}')+'%')