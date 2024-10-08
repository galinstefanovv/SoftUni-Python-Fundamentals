race = input().split()
numbers = []
for i in race:
    numbers.append(int(i))
finish = len(numbers) // 2
f_car = numbers[0:finish]
l_car = numbers[-1:finish:-1]

score_f_car = 0
score_l_car = 0

for current_time in f_car:
    score_f_car += current_time
    if current_time == 0:
        score_f_car *= 0.8

for current_time in l_car:
    score_l_car += current_time
    if current_time == 0:
        score_l_car *= 0.8

if score_f_car > score_l_car:
    print(f'The winner is right with total time: {score_l_car:.1f}')
else:
    print(f'The winner is left with total time: {score_f_car:.1f}')