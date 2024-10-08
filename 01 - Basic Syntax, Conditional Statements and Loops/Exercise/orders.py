n = int(input())
total_price = 0
for i in range(n):
    price = float(input())
    days = int(input())
    capsules = int(input())
    if 100 < price or price < 0.01:
        continue
    elif 31 < days or days < 1:
        continue
    elif 2000 < capsules or capsules < 1:
        continue
    total_price += price * days * capsules
    print(f'The price for the coffee is: ${price * days * capsules:.2f}')
print(f'Total: ${total_price:.2f}')