import sys
sys.setrecursionlimit(10**7)
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())

graph = [[0] * m for _ in range(n)]
result = []
count = 0
cnt = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    global cnt
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1


for _ in range(k):
    a, b, c, d = map(int, sys.stdin.readline().split())
    for i in range(b, d):
        for j in range(a, c):
            graph[i][j] = 1


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            graph[i][j] = 1
            bfs(i, j)
            result.append(cnt)
            cnt = 1
            count += 1

result.sort()

print(count)
for i in range(len(result)):
    print(result[i], end = ' ')