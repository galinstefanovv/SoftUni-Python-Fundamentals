string = input()
final_message = ''
for character in string:
    new_symbol = chr(ord(character) + 3)
    final_message += new_symbol
print(final_message)