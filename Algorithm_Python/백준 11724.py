import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
count = 0

def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, len(visited)):
    if visited[i] == False:
        count += 1
        dfs(graph, i, visited)

print(count)