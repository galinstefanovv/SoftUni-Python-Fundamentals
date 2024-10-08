input = float(input())

if input == 0:
    print('zero')
elif input > 0:
    if input < 1:
        print('small positive')
    elif input > 1000000:
        print('large positive')
    else:
        print('positive')
else:
    if abs(input) < 1:
        print('small negative')
    elif abs(input) > 1000000:
        print('large negative')
    else:
        print('negative')