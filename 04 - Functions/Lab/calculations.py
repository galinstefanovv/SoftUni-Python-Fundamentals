def calculations(operator, number1, number2):
    if operator == "multiply":
        return number1 * number2
    elif operator == "divide":
        return int(number1 / number2)
    elif operator == "add":
        return number1 + number2
    elif operator == "subtract":
        return number1 - number2
command = input()
first = int(input())
second = int(input())
print(calculations(command, first, second))

