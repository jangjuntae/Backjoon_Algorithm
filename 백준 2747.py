import sys
sys.setrecursionlimit(10**5)


def fibo(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if fibo_list[x] == 0:
        fibo_list[x] = fibo(x-1) + fibo(x-2)
    return fibo_list[x]


n = int(sys.stdin.readline())
fibo_list = [0] * 46
print(fibo(n))