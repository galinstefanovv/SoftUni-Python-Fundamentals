n = int(input())
grades = {}
for _ in range(1, n + 1):
    student = input()
    grade = float(input())
    if student not in grades:
        grades[student] = []
    grades[student].append(grade)

for name, average in grades.items():
    average_grade = sum(average) / len(average)
    if average_grade >= 4.5:
        print(f"{name} -> {average_grade:.2f}")

