input_line = input()
count = 0
while input_line != 'END':
    if input_line.isupper():
        if input_line == 'CODING' or input_line == 'DOG' or input_line == 'CAT' or input_line == 'MOVIE':
            count += 2
    elif input_line.islower():
        if input_line == 'coding' or input_line == 'dog' or input_line == 'cat' or input_line == 'movie':
            count += 1
    input_line = input()
if count > 5:
    print(f'You need extra sleep')
else:
    print(f'{count}')