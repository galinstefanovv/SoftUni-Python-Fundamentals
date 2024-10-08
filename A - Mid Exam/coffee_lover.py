def include(coffee):
    coffees.append(coffee)
    return coffees


def remove(cmd, index):
    if index < len(coffees):
        if cmd == "first":
            del coffees[:index]
        elif cmd == "last":
            del coffees[len(coffees) - index:]


def prefer(index1, index2):
    if index1 in range(len(coffees)) and index2 in range(len(coffees)):
        coffees[index1], coffees[index2] = coffees[index2], coffees[index1]
    return coffees


def reverse():
    coffees.reverse()
    return coffees


coffees = input().split()
number = int(input())

for i in range(1, number + 1):
    command = input().split()
    if command[0] == "Include":
        include(command[1])
    elif command[0] == "Remove":
        remove(command[1], int(command[2]))
    elif command[0] == "Prefer":
        prefer(int(command[1]), int(command[2]))
    elif command[0] == "Reverse":
        reverse()
print(f'Coffees:')
print(f"{' '.join(coffees)}")
