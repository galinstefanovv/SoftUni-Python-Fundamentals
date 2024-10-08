sequence = [int(n) for n in input().split(' ')]
command = input()
new_list = []
count = 0
while command != "End":
    indices = int(command)
    if indices >= len(sequence):
        command = input()
        continue
    else:
        if sequence[indices] == -1:
            command = input()
            continue
        else:
            last_value = sequence[indices]
            sequence[indices] = -1
            count += 1
            for i in range(len(sequence)):
                if sequence[i] > last_value:
                    sequence[i] -= last_value
                elif sequence[i] <= last_value and sequence[i] != sequence[indices]:
                    sequence[i] += last_value

    command = input()

print(f"Shot targets: {count} -> {' '.join(str(n) for n in sequence)}")
