import sys

n = sys.stdin.readline().strip()
length = len(n) - 1
result = 0

for i in range(length):
    result += 9 * (10 ** i) * (i + 1)

result += ((int(n) - (10 ** length)) + 1) * (length + 1)

print(result)