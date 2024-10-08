food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())
food_gr = food * 1000
hay_gr = hay * 1000
cover_gr = cover * 1000
weight_gr = weight * 1000
enough = True
for i in range(1, 31):
    food_gr -= 300
    if i % 2 == 0:
        hay_gr -= food_gr * 0.05
    if i % 3 == 0:
        cover_gr -= weight_gr * 1/3
    if food_gr <= 0 or hay_gr <= 0 or cover_gr <= 0:
        enough = False
        break
if enough:
    print(f'Everything is fine! Puppy is happy! Food: {food_gr/1000:.2f}, Hay: {hay_gr/1000:.2f}, Cover: {cover_gr/1000:.2f}.')
else:
    print(f'Merry must go to the pet store!')