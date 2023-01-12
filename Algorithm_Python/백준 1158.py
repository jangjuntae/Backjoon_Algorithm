from collections import deque

N, K = map(int, input().split())
yo = deque()
a = ''

for i in range(N, 0, -1):
    yo.append(i)

while len(yo) > 0:
    for i in range(K - 1):
        yo.appendleft(yo.pop())
    a = a + (str(yo.pop()))
    if len(yo) > 0:
        a = a + ', '
    else:
        break

print('<'+a+'>')