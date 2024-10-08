emp1 = int(input())
emp2 = int(input())
emp3 = int(input())
students = int(input())
total_emp = emp1 + emp2 + emp3
hours = 0
total_students = 0

while students > 0:
    students -= total_emp
    hours += 1
    if hours % 4 == 0:
        hours += 1


print(f'Time needed: {hours}h.')