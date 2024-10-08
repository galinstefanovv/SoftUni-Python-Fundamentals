pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health = int(input())
lost = False
command = input()

while command != 'Retire':
    tokens = command.split(' ')
    if tokens[0] == 'Fire':
        idx = int(tokens[1])
        damage = int(tokens[2])
        if 0 <= idx < len(warship):
            warship[idx] -= damage
            if warship[idx] <= 0:
                print('You won! The enemy ship has sunken.')
                lost = True
                break
    elif tokens[0] == 'Defend':
        start_idx = int(tokens[1])
        end_idx = int(tokens[2])
        damage = int(tokens[3])
        if 0 <= start_idx < len(pirate_ship) and 0 <= end_idx < len(pirate_ship):
            for idx in range(start_idx, end_idx + 1):
                pirate_ship[idx] -= damage
                if pirate_ship[idx] <= 0:
                    print('You lost! The pirate ship has sunken.')
                    lost = True
                    break
            if lost:
                break
    elif tokens[0] == 'Repair':
        idx = int(tokens[1])
        health = int(tokens[2])
        if 0 <= idx < len(pirate_ship):
            if pirate_ship[idx] + health > max_health:
                health = max_health - pirate_ship[idx]
            pirate_ship[idx] += health
    elif tokens[0] == 'Status':
        minimum = max_health * 0.2
        count = len([x for x in pirate_ship if x < minimum])
        print(f'{count} sections need repair.')

    command = input()
if not lost:
    print(f'Pirate ship status: {sum(pirate_ship)}')
    print(f'Warship status: {sum(warship)}')


# ship = [int(n) for n in input().split('>')]
# warship = [int(n) for n in input().split('>')]
# ship_capacity = int(input())
# command = input()
# stalemate = False
# lost = False
# while True:
#     if command == "Retire":
#         stalemate = True
#         break
#     cmd = command.split()
#     if cmd[0] == "Fire":
#         if int(cmd[1]) in range(len(warship)):
#             warship[int(cmd[1])] -= int(cmd[2])
#             if warship[int(cmd[1])] <= 0:
#                 print(f'You won! The enemy ship has sunken.')
#                 break
#     elif cmd[0] == "Defend":
#         if int(cmd[1]) in range(len(ship)) and int(cmd[2]) in range(len(ship)):
#             for element in range(len(ship[int(cmd[1]):int(cmd[2]) + 1])):
#                 ship[element] -= int(cmd[3])
#                 if ship[element] <= 0:
#                     print(f'You lost! The pirate ship has sunken.')
#                     lost = True
#                     break
#             if lost:
#                 break
#     elif cmd[0] == "Repair":
#         idx = int(cmd[1])
#         health = int(cmd[2])
#         if idx >= 0 and idx < len(ship):
#             if ship[idx] + health > ship_capacity:
#                 health = ship_capacity - ship[idx]
#             ship[idx] += health
#     elif cmd[0] == "Status":
#         minimum = ship_capacity * 0.2
#         count = len([x for x in ship if x < minimum])
#         print(f'{count} sections need repair.')
#     command = input()
#
# if stalemate:
#     print(f'Pirate ship status: {sum(int(n) for n in ship)}')
#     print(f'Warship status: {sum(int(n) for n in warship)}')