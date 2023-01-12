from collections import deque
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

graph = []
count = 0
value = 0
value_list = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global value
    queue = deque()
    queue.append((x, y))
    value += 1
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                value += 1
                queue.append((nx, ny))


for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)
            count += 1
            value_list.append(value)
            value = 0

value_list.append(0)
print(count)
print(max(value_list))
