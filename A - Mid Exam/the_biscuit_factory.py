from math import floor

biscuits_produced = int(input())
workers_count = int(input())
competing_biscuits = int(input())
per_day = biscuits_produced * workers_count
production = 0
total = 0
for days in range(1, 31):
    if days % 3 == 0:
        production += floor(per_day * 0.75)
    else:
        production += floor(biscuits_produced * workers_count)
print(f'You have produced {production} biscuits for the past month.')
diff = abs(production - competing_biscuits)
if production > competing_biscuits:
    print(f'You produce {diff / competing_biscuits * 100:.2f} percent more biscuits.')
else:
    print(f'You produce {diff / competing_biscuits * 100:.2f} percent less biscuits.')
