from collections import deque
import sys
sys.setrecursionlimit(10**7)

n, m, k = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visit_depth = [0] * (n + 1)
count = 1


def dfs(x):
    global count
    count += 1
    for i in graph[x]:
        if visit_depth[i] == 0:
            visit_depth[i] = count
            dfs(i)


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

visit_depth[k] = 1
dfs(k)

for i in range(1, n + 1):
    print(visit_depth[i])
