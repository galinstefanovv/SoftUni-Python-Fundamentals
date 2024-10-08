energy = int(input())
command = input()
win = 0
over = False
while command != "End of battle":
    distance = int(command)
    if distance > energy:
        over = True
        break
    energy -= distance
    win += 1
    if win % 3 == 0:
        energy += win
    command = input()
if over:
    print(f'Not enough energy! Game ends with {win} won battles and {energy} energy')
else:
    print(f'Won battles: {win}. Energy left: {energy}')