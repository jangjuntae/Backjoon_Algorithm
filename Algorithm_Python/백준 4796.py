case = 1
while True:
    l, p, v = input().split()
    l, p, v = int(l), int(p), int(v)
    if (l, p, v) == (0, 0, 0):
        break

    res = (v//p)*l + v%p if v%p <= l else (v//p)*l + l
    print("Case %d: %d"%(case, res))
    case += 1