dungeon = input().split("|")
health = 100
bitcoins = 0
over = False
best_room = 0
for element in dungeon:
    my_element = element.split()
    best_room += 1
    if my_element[0] == "potion":
        health_points = int(my_element[1])
        if health + health_points > 100:
            health_points = 100 - health
            health = 100
        else:
            health += health_points
        print(f'You healed for {health_points} hp.')
        print(f'Current health: {health} hp.')
    elif my_element[0] == "chest":
        bitcoins += int(my_element[1])
        print(f'You found {my_element[1]} bitcoins.')
    else:
        health -= int(my_element[1])
        if health > 0:
            print(f'You slayed {my_element[0]}.')
        else:
            print(f'You died! Killed by {my_element[0]}.')
            over = True
            break
if not over:
    print(f"You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')
else:
    print(f'Best room: {best_room}')
