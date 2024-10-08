budget = float(input())
price = float(input())
egg = price * 0.75
milk = price * 1.25 / 4
one_bread_price = egg + milk + price
breads_counter = 0
colored = 0
while budget >= one_bread_price:
    breads_counter += 1
    colored += 3
    if breads_counter % 3 == 0:
        colored -= breads_counter - 2
    budget -= one_bread_price
print(f'You made {breads_counter} loaves of Easter bread! Now you have {colored} eggs and {budget:.2f}BGN left.')