N = list(map(int, input()))
N.sort(reverse=True)
a = sum(N)

if a % 3 == 0:
    if N[-1] == 0:
        b = ''.join(map(str, N))
        b = int(b)
        print(b)
    else:
        print(-1)
else:
    print(-1)