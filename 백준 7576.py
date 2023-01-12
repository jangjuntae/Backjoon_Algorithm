from collections import deque
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
queue = deque()
graph = []
max_day = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if (0 <= nx < m) and (0 <= ny < n) and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


for i in range(m):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i, j))

bfs()

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
        max_day = max(max_day, graph[i][j])

print(max_day - 1)