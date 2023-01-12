import sys
sys.setrecursionlimit(10**7)

dx = [1, -1, 0, 0, 1, -1, -1, 1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

def dfs(x, y):
    graph[x][y] = 0

    for i in range(8):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
            dfs(nx, ny)


while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    graph = []
    count = 0

    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)