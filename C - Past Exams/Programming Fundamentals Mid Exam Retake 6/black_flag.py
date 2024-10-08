days = int(input())
plunder = int(input())
expected = int(input())
total_plunder = 0
for i in range(1, days + 1):
    total_plunder += plunder
    if i % 3 == 0:
        total_plunder += plunder * 0.5
    if i % 5 == 0:
        total_plunder -= total_plunder * 0.3
if total_plunder >= expected:
    print(f'Ahoy! {total_plunder:.2f} plunder gained.')
else:
    print(f'Collected only {(total_plunder / expected) * 100:.2f}% of the plunder.')
