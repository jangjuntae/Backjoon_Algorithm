import sys

n, m = map(int, sys.stdin.readline().split())

books = list(map(int, sys.stdin.readline().split()))
book_plus = []
book_minus = []
distance = []
max_value = 0
result = 0

for book in books:
    if book > 0:
        book_plus.append(book)
    else:
        book_minus.append(book)
    if abs(book) > abs(max_value):
        max_value = book

book_plus.sort(reverse=True)
book_minus.sort()

for i in range(0, len(book_plus), m):
    if book_plus[i] != max_value:
        distance.append(book_plus[i])

for i in range(0, len(book_minus), m):
    if book_minus[i] != max_value:
        distance.append(abs(book_minus[i]))

result += abs(max_value) + (sum(distance) * 2)

print(result)

