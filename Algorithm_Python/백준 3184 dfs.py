import sys
sys.setrecursionlimit(10**6)
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []

wolf = 0
sheep = 0
wolf_number = []
sheep_number = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global wolf
    global sheep

    if graph[x][y] != '#':
        if graph[x][y] == 'v':
            wolf += 1
        if graph[x][y] == 'o':
            sheep += 1

    graph[x][y] = '#'

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '#':
            dfs(nx, ny)


for i in range(n):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == '.' or graph[i][j] == 'v' or graph[i][j] == 'o':
            dfs(i, j)
            wolf_number.append(wolf)
            sheep_number.append(sheep)
            wolf = 0
            sheep = 0

for i in range(len(wolf_number)):
    if wolf_number[i] >= sheep_number[i]:
        sheep_number[i] = 0
    if wolf_number[i] < sheep_number[i]:
        wolf_number[i] = 0

print(sum(sheep_number), sum(wolf_number))