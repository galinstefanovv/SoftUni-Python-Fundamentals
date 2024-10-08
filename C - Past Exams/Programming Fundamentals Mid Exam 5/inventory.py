journal = input().split(", ")
command = input()

while command != "Craft!":
    cmd = command.split()
    activity = cmd[0]

    if activity == "Collect":
        if not cmd[2] in journal:
            journal.append(cmd[2])
    elif activity == "Drop":
        if cmd[2] in journal:
            journal.remove(cmd[2])
    elif activity == "Combine":
        split = cmd[3].split(':')
        if split[0] in journal:
            journal_index = journal.index(split[0])
            journal.insert(journal_index + 1, split[1])
    elif activity == "Renew":
        if cmd[2] in journal:
            journal.remove(cmd[2])
            journal.append(cmd[2])
    command = input()
print(f"{', '.join(str(n) for n in journal)}")