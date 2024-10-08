rooms = int(input())
no_space = False
space_left = 0
for room in range(1, rooms + 1):
    command = input().split()
    chairs = command[0]
    visitors = int(command[1])
    if len(chairs) < visitors:
        needed = visitors - len(chairs)
        print(f'{needed} more chairs needed in room {room}')
        no_space = True
    else:
        space_left += len(chairs) - visitors
if not no_space:
    print(f'Game On, {space_left} free chairs left')
