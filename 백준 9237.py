n = int(input())

time = list(map(int, input().split()))

time.sort(reverse=True)
# 4 3 3 2
count = 1

for i in range(n):
    time[i] += count
    count += 1

print(max(time) + 1)