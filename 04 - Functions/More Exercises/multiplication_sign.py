first = int(input())
second = int(input())
third = int(input())

my_list = [first, second, third]
positive = 0
negative = 0
zero = False
for i in my_list:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
    else:
        zero = True

if negative == 1 or negative == 3:
    print(f'negative')
elif zero:
    print(f'zero')
else:
    print(f'positive')





