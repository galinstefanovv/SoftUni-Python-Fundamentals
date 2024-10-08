string = input()
repeated = ""
while string != 'End':
    for i in range(len(string)):
        repeated += string[i] + string[i]
    if string != 'SoftUni':
        print(repeated)
    repeated = ""
    string = input()