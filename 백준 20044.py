n = int(input())

student = list(map(int, input().split()))

a = len(student) // 2

student_low = []
student_high =  []
result = []

student.sort()

for i in range(a):
  student_low.append(student[i])

student.sort(reverse=True)

for i in range(a):
  student_high.append(student[i])

for i in range(a):
  result.append(student_low[i] + student_high[i])

print(min(result))