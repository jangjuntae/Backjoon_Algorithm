a, b, c = map(int, input().split())

if c > b:
  print(a//(c-b)+1)
else:
  print(-1)