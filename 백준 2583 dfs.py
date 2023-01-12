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


def dfs(x, y):
    global cnt
    graph[x][y] = 1

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            cnt += 1
            dfs(nx, ny)


for i in range(k):
    a, b, c, d = map(int, sys.stdin.readline().split())

    for j in range(b, d):
        for t in range(a, c):
            graph[j][t] = 1


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(i, j)
            count += 1
            result.append(cnt)
            cnt = 1

result.sort()

print(count)
for i in range(len(result)):
    print(result[i], end = ' ')