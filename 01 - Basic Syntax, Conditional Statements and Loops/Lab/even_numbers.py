n = int(input())
odd = False
for i in range(n):
    number = int(input())
    if number % 2 != 0:
        odd = True
        print(f'{number} is odd!')
        break
if not odd:
    print('All numbers are even.')
