from math import ceil
number = int(input())
lectures = int(input())
bonus = int(input())
total_bonus = []
att_list = []
if lectures != 0:
    for i in range(1, number + 1):
        attendances = int(input())
        total_bonus.append(attendances / lectures * (5 + bonus))
        att_list.append(attendances)
    top_student = max(total_bonus)
    student_index = total_bonus.index(top_student)

    print(f"Max Bonus: {ceil(top_student)}.")
    print(f"The student has attended {att_list[student_index]} lectures.")
else:
    print(f"Max Bonus: 0.")
    print(f"The student has attended 0 lectures.")