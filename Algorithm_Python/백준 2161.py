from collections import deque
N = int(input())
card = deque()
stack = ''

for i in range(N, 0, -1):
    card.append(i)

while len(card) > 1:
    stack = stack + str(card.pop()) + ' '
    card.appendleft(card.pop())

stack = stack + str(card.pop())

print(stack)