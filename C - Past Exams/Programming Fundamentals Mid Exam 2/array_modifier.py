values = [int(n) for n in input().split()]
command = input()
while command != "end":
    modify = command.split()
    if modify[0] == "swap":
        index1 = int(modify[1])
        index2 = int(modify[2])
        values[index1], values[index2] = values[index2], values[index1]
    if modify[0] == "multiply":
        index1 = int(modify[1])
        index2 = int(modify[2])
        values[index1] = values[index1] * values[index2]
    if modify[0] == "decrease":
        for i in range(len(values)):
            values[i] -= 1
    command = input()

print(f"{', '.join(str(n) for n in values)}")