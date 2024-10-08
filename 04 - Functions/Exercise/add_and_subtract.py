def sum_numbers(first, second):
    return first + second


def subtract(first, second, third):
    first_sum = sum_numbers(first, second)
    return first_sum - third


first_number = int(input())
second_number = int(input())
third_number = int(input())
result = subtract(first_number, second_number, third_number)
print(result)
