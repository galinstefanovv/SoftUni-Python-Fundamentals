integers = [int(n) for n in input().split()]
removed_sum = 0
while len(integers) > 0:
    command = int(input())
    if command < 0:
        removed = integers.pop(0)
        integers.insert(0, integers[-1])
    elif command > len(integers) - 1:
        removed = integers.pop()
        integers.append(integers[0])
    else:
        removed = integers.pop(command)
    for number in range(len(integers)):
        if integers[number] <= removed:
            integers[number] += removed
        else:
            integers[number] -= removed
    removed_sum += removed
print(removed_sum)
