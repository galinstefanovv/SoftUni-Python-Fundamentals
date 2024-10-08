groceries = input().split('!')
command = input()

while command != "Go Shopping!":
    cmd = command.split()
    if cmd[0] == "Urgent":
        if not cmd[1] in groceries:
            groceries.insert(0, cmd[1])
    elif cmd[0] == "Unnecessary":
        if cmd[1] in groceries:
            groceries.remove(cmd[1])
    elif cmd[0] == "Correct":
        if cmd[1] in groceries:
            for i in range(len(groceries)):
                if cmd[1] == groceries[i]:
                    groceries[i] = cmd[2]
    elif cmd[0] == "Rearrange":
        if cmd[1] in groceries:
            groceries.remove(cmd[1])
            groceries.append(cmd[1])
    command = input()
print(f"{', '.join(str(n) for n in groceries)}")