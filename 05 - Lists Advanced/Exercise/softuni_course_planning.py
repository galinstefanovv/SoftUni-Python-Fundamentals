def add(string):
    if not string in course:
        course.append(string)
    return course


def insert(string, index):
    if index < len(course):
        if not string in course:
            course.insert(index, string)
    return course


def remove(string):
    exercise = string + "-Exercise"
    if string in course:
        course.remove(string)
        if exercise in course:
            course.remove(exercise)
    return course


def swap(first, second):
    if first in course and second in course:
        exercise = first + "-Exercise"
        exercise_two = second + "-Exercise"
        index_1 = course.index(first)
        index_2 = course.index(second)
        if exercise in course and exercise_two in course:
            course[index_1], course[index_2] = \
                course[index_2], course[index_1]
            course.remove(exercise)
            course.remove(exercise_two)
            course.insert(index_2 + 1, exercise)
            course.insert(index_1 + 1, exercise_two)
        elif exercise in course:
            course[index_1], course[index_2], = course[index_2], course[index_1]
            course.remove(exercise)
            course.insert(index_2 + 1, exercise)
        elif exercise_two in course:
            course[index_1], course[index_2] = course[index_2], course[index_1]
            course.remove(exercise_two)
            course.insert(index_1 + 1, exercise_two)
        else:
            course[index_1], course[index_2] = course[index_2], course[index_1]
    return course


def exercise(string):
    exercise = string + "-Exercise"
    if string not in course:
        if exercise not in course:
            course.append(string)
            course.append(exercise)
    else:
        if exercise not in course:
            index_1 = course.index(string)
            course.insert(index_1 + 1, exercise)
    return course


course = input().split(", ")
command = input()

while command != "course start":
    cmd = command.split(':')
    if cmd[0] == "Add":
        add(cmd[1])
    elif cmd[0] == "Insert":
        insert(cmd[1], int(cmd[2]))
    elif cmd[0] == "Remove":
        remove(cmd[1])
    elif cmd[0] == "Swap":
        swap(cmd[1], cmd[2])
    elif cmd[0] == "Exercise":
        exercise(cmd[1])

    command = input()
for element in course:
    index = course.index(element)
    course[index] = str(index + 1) + "." + element
print("\n".join(course))