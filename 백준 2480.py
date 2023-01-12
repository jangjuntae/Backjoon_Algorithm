import sys

n, m, k = map(int, sys.stdin.readline().split())

if n == m == k:
    print(10000+(n*1000))
elif n == m and n != k:
    print(1000+(n*100))
elif n == k and n != m:
    print(1000+(n*100))
elif k == m and k != n:
    print(1000+(k*100))
elif n != m != k:
    print(max(n, m, k)*100)