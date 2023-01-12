from collections import deque
import sys
sys.setrecursionlimit(10**7)

n, m, k = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
visit_num = [0] * (n + 1)
visit_depth = [-1] * (n + 1)
count = 1
visit_num[k] = 1
visit_depth[k] = 0
result = 0


def bfs(x):
    global count
    queue = deque()
    queue.append(x)
    visited[x] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                count += 1
                visited[i] = True
                visit_num[i] = count
                visit_depth[i] = visit_depth[x] + 1
                queue.append(i)


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()

bfs(k)

for i in range(1, n + 1):
    result += visit_num[i] * visit_depth[i]

print(result)