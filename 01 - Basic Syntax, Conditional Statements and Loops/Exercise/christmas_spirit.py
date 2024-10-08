quantity = int(input())
days_left = int(input())
price = 0
points = 0
total = 0
for i in range(1, days_left + 1):
    if i % 2 == 0:
        price += 2 * quantity
        points += 5
    if i % 3 == 0:
        price += 8 * quantity
        points += 30
    if i % 5 == 0:
        price += 15 * quantity
        points += 17
    if i % 10 == 0:
        price -= 23 * quantity
        points -= 20
    if i % 11 == 0:
        quantity = quantity * 2
    if i == 10:
        points -= 30

print(f'Total cost: {price}')
print(f'Total spirit: {points}')