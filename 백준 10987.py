import sys

n = sys.stdin.readline().strip()
count = 0

for i in range(len(n)):
    if n[i] =='a' or n[i] == 'e' or n[i] == 'i' or n[i] == 'o' or n[i] == 'u':
        count += 1

print(count)