input_line = int(input())
text = ''
if input_line <= 14:
    text = 'toddy'
elif input_line <= 18:
    text ='coke'
elif input_line <= 21:
    text ='beer'
else:
    text = 'whisky'

print(f'drink {text}')