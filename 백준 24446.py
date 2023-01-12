from collections import deque
import sys
sys.setrecursionlimit(10**7)
n, m, k = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
visit_value = [-1] * (n + 1)


def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = True
    visit_value[x] = 0
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visit_value[i] = visit_value[x] + 1
                visited[i] = True
                queue.append(i)


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(k)

for i in range(1, n + 1):
    print(visit_value[i])