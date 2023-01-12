A = int(input())
B = int(input())
C = int(input())

D = A*B*C
D = str(D)

for i in range(0, 10):
    print(D.count(str(i)))