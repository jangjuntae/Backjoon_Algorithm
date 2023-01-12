import heapq

n = int(input())

stack = []
result = 0

for _ in range(n):
    heapq.heappush(stack, int(input()))

while True:
    if len(stack) == 1:
        break
    num_1 = heapq.heappop(stack)
    num_2 = heapq.heappop(stack)
    count = num_1 + num_2
    heapq.heappush(stack, count)
    result += count

print(result)