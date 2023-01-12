import sys

while True:
    num = sys.stdin.readline().strip()
    if int(num) == 0:
        break
    while len(num) > 1:
        value = 0
        num = str(num)

        for i in range(len(num)):
            value += int(num[i])

        num = str(value)

    print(int(num))