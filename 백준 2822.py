import sys

score_be = []
score_af = []
answer = []

for i in range(8):
    score_be.append(int(sys.stdin.readline()))
    score_af.append(score_be[i])

score_af.sort()

result = 0

for i in range(3, 8):
    result += score_af[i]
    answer.append(score_be.index(score_af[i]))

answer.sort()

print(result)
for i in range(len(answer)):
    print(answer[i] + 1, end = ' ')

