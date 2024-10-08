string = input()
number = int(input())
repeat_string = lambda string_to_repeat, repeat_number: string_to_repeat * repeat_number
result = repeat_string(string, number)
print(result)
