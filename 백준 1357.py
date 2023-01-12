import sys

x, y = map(str, sys.stdin.readline().split())

value = str(int(x[::-1]) + int(y[::-1]))

print(int(value[::-1]))