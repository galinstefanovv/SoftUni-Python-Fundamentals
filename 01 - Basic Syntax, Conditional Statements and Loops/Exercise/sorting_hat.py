input_line = input()
volde = False
while input_line != "Welcome!":
    if input_line == "Voldemort":
        volde = True
        print(f'You must not speak of that name!')
        break

    if len(input_line) < 5:
        print(f'{input_line} goes to Gryffindor.')
    elif len(input_line) == 5:
        print(f'{input_line} goes to Slytherin.')
    elif len(input_line) == 6:
        print(f'{input_line} goes to Ravenclaw.')
    elif len(input_line) > 6:
        print(f'{input_line} goes to Hufflepuff.')
    input_line = input()
if not volde:
    print(f'Welcome to Hogwarts.')