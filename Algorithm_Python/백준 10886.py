import sys

n = int(sys.stdin.readline())
value = []

for i in range(n):
    value.append(int(sys.stdin.readline()))

if value.count(1) > value.count(0):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")