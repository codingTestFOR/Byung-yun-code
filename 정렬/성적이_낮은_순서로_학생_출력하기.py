class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

student_list: list[Student]
student_list = []

# 입력
N = int(input())
numbers = []
for i in range(N):
    a, b = input().split()
    s = Student(a, b)
    student_list.append(s)

result = sorted(student_list, key=lambda stu:stu.score)

for i in result:
    print(i.name, end=' ')
