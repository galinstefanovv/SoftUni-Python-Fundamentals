event = input().split("|")
energy = 100
coins = 100
handle = True
for i in range(len(event)):
    eventname, number = event[i].split("-")
    number = int(number)
    if eventname == "rest":
            current_energy = energy
            energy += number
            if energy > 100:
                energy = 100
            gained_energy = energy - current_energy
            print(f'You gained {gained_energy} energy.')
            print(f'Current energy: {energy}.')
    elif eventname == "order":
        if energy >= 30:
            energy -= 30
            coins += number
            print(f'You earned {number} coins.')
        else:
            energy += 50
            print(f'You had to rest!')

    else:
        if coins >= number:
            coins -= number
            print(f'You bought {eventname}.')
        else:
            print(f'Closed! Cannot afford {eventname}.')
            handle = False
            break
if handle:
    print(f'Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')

