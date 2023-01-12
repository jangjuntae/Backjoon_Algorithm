from collections import deque

N, K = map(int, input().split())
q = deque()
stack = ''

for i in range(N, 0, -1):
    q.append(i)

while len(q) > 0:
    for i in range(K - 1):
        q.appendleft(q.pop())
    stack = stack + (str(q.pop()))
    if len(q) == 0:
        break
    stack = stack + ', '

print('<'+stack+'>')