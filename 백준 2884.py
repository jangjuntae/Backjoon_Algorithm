a, b = map(int, input().split())

if b >= 45:
  a = a
  b = b - 45
elif b < 45:
  a = a - 1
  if a < 0:
    a = 23
  b = b + 15

print(int(a), int(b))