import sys
a = int(input())

for i in range(0, a):
  A, B = map(int, sys.stdin.readline().split())
  print(A + B)