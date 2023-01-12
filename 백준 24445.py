from collections import deque
import sys
sys.setrecursionlimit(10**7)
n, m, k = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
stack = [0] * (n + 1)
count = 1


def bfs(x):
    global count
    queue = deque()
    queue.append(x)
    visited[x] = True
    stack[x] = count
    while queue:
        num = queue.popleft()
        for i in graph[num]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                count += 1
                stack[i] = count


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort(reverse=True)

bfs(k)

for i in range(1, len(stack)):
    print(stack[i])