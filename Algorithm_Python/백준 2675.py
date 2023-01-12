a = int(input())

for i in range(a):
  b, s = input().split()
  for j in range(0, len(s)):
    P = s[j]*int(b)
    print(P, end = '')
  print()