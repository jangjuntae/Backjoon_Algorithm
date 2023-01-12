N = int(input())

def fact(N):
    if N == 1 or N == 0:
        return 1
    else:
        return N * fact(N-1)

print(fact(N))