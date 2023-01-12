while True:
    num = str(input())
    if num =='0':
        break
    if num == num[::-1]:
        print('yes')
    else:
        print('no')