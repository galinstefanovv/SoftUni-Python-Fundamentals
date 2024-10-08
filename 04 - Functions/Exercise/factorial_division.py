def factorial(number1, number2):
    divide_first = 1
    divide_second = 1
    for factorial_one in range(1, number1 + 1):
        divide_first *= factorial_one
    for factorial_two in range(1, number2 + 1):
        divide_second *= factorial_two
    final_result = divide_first // divide_second
    return final_result


first_number = int(input())
second_number = int(input())

result = factorial(first_number, second_number)
print(f'{result:.2f}')
