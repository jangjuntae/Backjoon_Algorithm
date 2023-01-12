import sys

n = int(sys.stdin.readline())

graph = []
result = []
count = 0

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global count
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)
            result.append(count)
            count = 0

result.sort()

print(len(result))
for i in range(len(result)):
    print(result[i])
