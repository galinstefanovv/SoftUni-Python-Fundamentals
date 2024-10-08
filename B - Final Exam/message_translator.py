number = int(input())
valid = False
for _ in range(1, number + 1):
    string = input()
    if ":" in string:
        splitted_string = string.split(":")
        if splitted_string[0][0] == "!" and splitted_string[0][-1] == "!" and splitted_string[0][1].isupper() and splitted_string[0][2:-1].islower() and len(splitted_string[0]) - 2 >= 3:
            if splitted_string[1][1:-1].isalpha() and splitted_string[1][0] == "[" and splitted_string[1][-1] == "]" and len(splitted_string[1]) - 2 >= 8:
                valid = True
            else:
                valid = False
        else:
            valid = False
    if valid:
        splitted = string.split(":")
        my_ords = []
        for word in splitted[1][1:-1].strip():
            my_ords.append(ord(word))
        print(f"{splitted[0][1:-1]}: {' '.join(str(x) for x in my_ords)}")
    else:
        print("The message is invalid")
