def password_validator(string):
    is_valid = True
    if len(string) < 6 or len(string) > 10:
        print(f'Password must be between 6 and 10 characters')
        is_valid = False
    if not string.isalnum():
        print(f'Password must consist only of letters and digits')
        is_valid = False
    counter = 0
    for character in string:
        if character.isdigit():
            counter += 1
    if counter < 2:
        print(f'Password must have at least 2 digits')
        is_valid = False
    return is_valid


some_pass = input()
password = password_validator(some_pass)

if password:
    print(f'Password is valid')
