string = input()
command = input()

while command != "Finish":
    if "Check" in command or "Make" in command:
        action, start = command.split()
        if action == "Make":
            if start == "Lower":
                string = string.lower()
            else:
                string = string.upper()
            print(string)
        elif action == "Check":
            if start in string:
                print(f"Message contains {start}")
            else:
                print(f"Message doesn't contain {start}")
    else:
        action, start, end = command.split()
        if action == "Replace":
            string = string.replace(start, end)
            print(string)
        elif action == "Cut":
            if int(start) > len(string) or int(end) > len(string) or int(start) < 0 or int(end) < 0:
                print(f"Invalid indices!")
            else:
                string = string[:int(start)] + string[int(end) + 1:]
                print(string)
        elif action == "Sum":
            if int(start) > len(string) or int(end) > len(string) or int(start) < 0 or int(end) < 0:
                print(f"Invalid indices!")
            else:
                value = string[int(start):int(end) + 1]
                ascii_sum = 0
                for n in value:
                    ascii_sum += ord(n)
                print(ascii_sum)
    command = input()