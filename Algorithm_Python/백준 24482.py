from collections import deque
import sys
sys.setrecursionlimit(10**7)

n, m, k = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
visit_depth = [-1] * (n + 1)


def dfs(x):
    visited[x] = True
    visit_depth[k] = 0
    for i in graph[x]:
        if not visited[i]:
            visit_depth[i] = visit_depth[x] + 1
            dfs(i)


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort(reverse=True)

dfs(k)

for i in range(1, n + 1):
    print(visit_depth[i])