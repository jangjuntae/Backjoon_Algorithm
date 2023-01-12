import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
visited = [False] * (n + 1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            visited[i] = True

def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        now = q.popleft()
        print(now, end = ' ')
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

dfs(v)
visited = [False] * (n + 1)
print()
bfs(v)