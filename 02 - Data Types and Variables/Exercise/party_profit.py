group = int(input())
days = int(input())
coins = 0
for i in range(1, days + 1):
    if i % 10 == 0:
        group -= 2
    if i % 15 == 0:
        group += 5
    if i % 3 == 0:
        coins -= 3 * group
    if i % 5 == 0:
        coins += 20 * group
        if i % 3 == 0:
            coins -= 2 * group

    coins += 50
    coins -= 2 * group


print(f'{group} companions received {int(coins / group)} coins each.')
