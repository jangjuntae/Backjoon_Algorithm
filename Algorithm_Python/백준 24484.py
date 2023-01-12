from collections import deque
import sys
sys.setrecursionlimit(10**7)

n, m, k = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
visit_depth = [-1] * (n + 1)
visit_sequence = [0] * (n + 1)
count = 1
result = 0


def dfs(x):
    global count
    visited[x] = True
    visit_depth[k] = 0
    visit_sequence[k] = 1
    for i in graph[x]:
        if not visited[i]:
            count += 1
            visit_depth[i] = visit_depth[x] + 1
            visit_sequence[i] = count
            dfs(i)


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort(reverse=True)

dfs(k)

for i in range(1, n + 1):
    result += visit_depth[i] * visit_sequence[i]

print(result)