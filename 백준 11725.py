from collections import deque
import sys

n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
parent = [[] for _ in range(n + 1)]


def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = True
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if not visited[i]:
                visited[i] = True
                parent[i] = a
                queue.append(i)


for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)

for i in range(2, n+1):
    print(parent[i])
