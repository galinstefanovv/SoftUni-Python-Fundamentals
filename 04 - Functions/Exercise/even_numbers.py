numbers = [int(i) for i in input().split()]


def check_even(number):
    if number % 2 == 0:
        return True

    return False


even_numbers_iterator = filter(check_even, numbers)

even_numbers = list(even_numbers_iterator)

print(even_numbers)
