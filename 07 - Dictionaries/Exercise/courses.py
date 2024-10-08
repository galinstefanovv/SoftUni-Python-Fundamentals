command = input()
courses = {}
while command != "end":
    course, student = command.split(" : ")
    if course not in courses.keys():
        courses[course] = []
    courses[course].append(student)
    command = input()

for course_name, student_name in courses.items():
    print(f"{course_name}: {len(student_name)}")
    for name in student_name:
        print(f"-- {name}")