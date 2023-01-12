while True:
    try:
        sentence = input()
        print(sentence)
    except EOFError:
        break