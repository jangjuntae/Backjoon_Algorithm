a, x = map(int, input().split())
r =list(map(int, (input().split())))

for i in range(0, a):
  if r[i] < x:
    print(r[i], end = ' ')