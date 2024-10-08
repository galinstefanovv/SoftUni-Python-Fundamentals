def single(number):
    odd = 0
    even = 0
    for i in number:
        if int(i) % 2 == 0:
            even += int(i)
        else:
            odd += int(i)
    return f'Odd sum = {odd}, Even sum = {even}'


numbers = input()
result = single(numbers)
print(result)

