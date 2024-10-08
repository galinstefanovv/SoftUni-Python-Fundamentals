targets = [int(n) for n in input().split(' ')]
command = input()

while command != "End":
    manipulate = command.split()
    cmd = manipulate[0]
    index1 = int(manipulate[1])
    index2 = int(manipulate[2])
    if cmd == "Shoot" and index1 in range(len(targets)):
        if targets[index1] - index2 > 0:
            targets[index1] -= index2
        else:
            targets.pop(index1)
    elif cmd == "Add":
        if index1 in range(len(targets)):
            targets.insert(index1, index2)
        else:
            print(f'Invalid placement!')
    elif cmd == 'Strike':
        radius = int(manipulate[2])
        before_radius = index1 - radius
        after_radius = index1 + radius

        if after_radius in range(len(targets)) and before_radius in range(len(targets)):
            targets = targets[0:before_radius] + targets[after_radius + 1::]
        else:
            print('Strike missed!')
    command = input()
print(f"{'|'.join(str(n) for n in targets)}")
