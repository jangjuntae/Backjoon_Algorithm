from collections import deque
import sys
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())
x, y = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
visit_value = [-1] * (n + 1)


def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            visit_value[i] = visit_value[x] + 1
            dfs(i)


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visit_value[x] = 0
dfs(x)
print(visit_value[y])