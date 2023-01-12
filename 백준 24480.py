import sys
sys.setrecursionlimit(10**7)

n, m, k = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 1


def dfs(x):
    global count
    visited[x] = count
    for i in graph[x]:
        if visited[i] == 0:
            count += 1
            dfs(i)


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort(reverse=True)

dfs(k)

for i in range(1, n + 1):
    print(visited[i])