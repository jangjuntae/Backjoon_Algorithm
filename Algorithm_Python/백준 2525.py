import sys

hour, minute = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())

x = c // 60
y = c % 60

minute += y
k = minute // 60
minute = minute % 60
hour += x + k

if hour > 23:
    hour -= 24

print(hour, minute)