for _ in range(3):
    yut = list(map(int, input().split()))

    n = yut.count(1)

    if n == 0:
        print('D')
    if n == 1:
        print('C')
    if n == 2:
        print('B')
    if n == 3:
        print('A')
    if n == 4:
        print('E')