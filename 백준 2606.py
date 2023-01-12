import sys

computer = int(sys.stdin.readline())
pair = int(sys.stdin.readline())

graph = [[] for _ in range(computer + 1)]

visited = [0] * (computer + 1)

for i in range(pair):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
        else:
            continue
    return True


dfs(1)
print(sum(visited) - 1)
