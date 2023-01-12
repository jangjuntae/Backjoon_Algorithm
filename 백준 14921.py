import sys

n = int(sys.stdin.readline())
value_list = list(map(int, sys.stdin.readline().split()))
left = 0
right = n - 1
result = 10**15
value_min = 0
value_max = 0
answer = 0

value_list.sort()

while left < right:
    value_left = value_list[left]
    value_right = value_list[right]

    near_0 = value_right + value_left

    if abs(near_0) < result:
        result = abs(near_0)
        answer = near_0
        value_min = value_left
        value_max = value_right

    if near_0 < 0:
        left += 1
    else:
        right -= 1

print(answer)



