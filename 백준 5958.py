from collections import deque
import sys
sys.setrecursionlimit(10**7)
n = int(sys.stdin.readline())

graph = []
count = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = '.'
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == '*':
                graph[nx][ny] = '.'
                queue.append((nx, ny))


for i in range(n):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == '*':
            bfs(i, j)
            count += 1

print(count)