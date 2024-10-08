input_line = input()
price_without_taxes = 0
taxes = 0
special = False
while input_line != "special" and input_line != "regular":
    prices = float(input_line)
    if prices < 0:
        print(f'Invalid price!')
        input_line = input()
    else:
        taxes += prices * 0.2
        price_without_taxes += prices
        input_line = input()
    if input_line == "special":
        special = True

total_price = taxes + price_without_taxes
if total_price == 0:
    print(f'Invalid order!')
else:
    if special:
        total_price *= 0.9
    print(f'Congratulations you\'ve just bought a new computer!')
    print(f'Price without taxes: {price_without_taxes:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print(f'-----------')
    print(f'Total price: {total_price:.2f}$')