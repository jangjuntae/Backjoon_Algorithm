from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)

n, m = map(int, sys.stdin.readline().split())

graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
near = 0
queue = deque()


def bfs():
    global near
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '#':
                near += 1


for i in range(n):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == "#":
            count += 1
            queue.append((i, j))

bfs()
print(count - (near // 2))