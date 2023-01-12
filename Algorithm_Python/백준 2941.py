croatia = list(str(input()))
croatia.append(" ")
croatia.append(" ")

num = 0

for i in range(len(croatia)):
    num += 1
    if croatia[i] == 'c' and croatia[i + 1] == '=':
        num = num - 1
    if croatia[i] == 'c' and croatia[i + 1] == '-':
        num = num - 1
    if croatia[i] == 'd' and croatia[i + 1] == 'z' and croatia[i + 2] == '=':
        num = num - 1
    elif croatia[i] == 'z' and croatia[i + 1] == '=':
        num = num - 1
    if croatia[i] == 'd' and croatia[i + 1] == '-':
        num = num - 1
    if croatia[i] == 'l' and croatia[i + 1] == 'j':
        num = num - 1
    if croatia[i] == 'n' and croatia[i + 1] == 'j':
        num = num - 1
    if croatia[i] == 's' and croatia[i + 1] == '=':
        num = num - 1
    if croatia[i] == " ":
        num = num - 1