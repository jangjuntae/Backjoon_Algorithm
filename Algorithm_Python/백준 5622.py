a = str(input()).upper()

dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
time = 0

for i in dial:
    for j in i:
        for b in range(len(a)):
            if a[b] == j:
                time = time + dial.index(i) + 3

print(time)