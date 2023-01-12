from collections import deque
import sys
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())
graph = []
count_dfs = 0
count_bfs = 0
visit_dfs = [[False] * n for i in range(n)]
visit_bfs = [[False] * n for j in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 일반 사람
def dfs(x, y):
    visit_dfs[x][y] = True
    if graph[x][y] == 'R':
        graph[x][y] = 'G'
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] == k:
            if not visit_dfs[nx][ny]:
                dfs(nx,  ny)


# 적록색약
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] == k:
                if not visit_bfs[nx][ny]:
                    visit_bfs[nx][ny] = True
                    queue.append((nx, ny))


for i in range(n):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))

for i in range(n):
    for j in range(n):
        if not visit_dfs[i][j]:
            k = graph[i][j]
            dfs(i, j)
            count_dfs += 1

for i in range(n):
    for j in range(n):
        if not visit_bfs[i][j]:
            k = graph[i][j]
            bfs(i, j)
            count_bfs += 1

print(count_dfs, count_bfs)