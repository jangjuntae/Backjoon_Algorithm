a = int(input())

arr = list(map(int, input().split()))

c = arr[0]
d = arr[0]

for i in range(0,a):
  if arr[i] < c:
    c = arr[i]
  elif arr[i] > d:
    d = arr[i]

print(c, d)