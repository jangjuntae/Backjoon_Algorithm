from collections import deque
import sys
sys.setrecursionlimit(10**7)

n, m, k = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
visit_num = [-1] * (n + 1)


def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            visit_num[i] = visit_num[x] + 1
            dfs(i)


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()

visit_num[k] = 0
dfs(k)

for i in range(1, n + 1):
    print(visit_num[i])
