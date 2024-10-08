budget = int(input())
command = input()
count = 0
overdraft = False
while command != 'End':
    price = int(command)
    count += price
    if count > budget:
        overdraft = True
        print(f'You went in overdraft!')
        break
    command = input()
if not overdraft:
    print(f'You bought everything needed.')
