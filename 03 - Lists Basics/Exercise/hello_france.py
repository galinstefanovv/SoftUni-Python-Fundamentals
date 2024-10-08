items = input().split("|")
budget = int(input())
item_price = 0
price_list = []
profit = 0
spend = 0
for everything in range(len(items)):
    item, price = items[everything].split("->")
    cost = float(price)
    if budget < cost:
        continue
    if item == "Clothes" and cost > 50:
        continue
    if item == "Shoes" and cost > 35:
        continue
    if item == "Accessories" and cost > 20.50:
        continue
    budget -= cost
    item_price = cost + cost * 0.4
    profit += item_price
    spend += cost
    price_list.append(item_price)

for el in price_list:
    print(f'{float(el):.2f}', end=" ")
print()
print(f'Profit: {abs(spend-profit):.2f}')
if profit + budget >= 150:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')
