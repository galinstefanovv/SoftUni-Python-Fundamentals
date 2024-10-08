def orders(product, quantity):
    if product == "coffee":
        return quantity * 1.50
    elif product == "water":
        return quantity * 1
    elif product == "coke":
        return quantity * 1.4
    elif product == "snacks":
        return quantity * 2


order = input()
amount = int(input())
result = orders(order, amount)
print(f'{result:.2f}')
