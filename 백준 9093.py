t = int(input())

for _ in range(t):
    a = list(map(str, input().split(' ')))
    d = ''
    for i in a:
        c = i[::-1]
        d = d + c + ' '
    d = d[:len(d)-1]
    print(d)