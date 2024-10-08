def perfect_number(number):
    is_perfect = False
    sums = 0
    for i in range(1, number):
        if number % i == 0:
            sums += i
    if sums == number:
        is_perfect = True
    return is_perfect


my_number = int(input())
my_result = perfect_number(my_number)

if my_result:
    print(f'We have a perfect number!')
else:
    print(f'It\'s not so perfect.')
