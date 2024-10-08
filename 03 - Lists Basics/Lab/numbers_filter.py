n = int(input())
my_list = []
filtered_list = []
for i in range(n):
    number = int(input())
    my_list.append(number)
command = input()
for j in range(len(my_list)):
    element = my_list[j]
    if command == "even":
        if element % 2 == 0:
            filtered_list.append(element)
    elif command == "odd":
        if element % 2 != 0:
            filtered_list.append(element)
    elif command == "negative":
        if element < 0:
            filtered_list.append(element)
    elif command == "positive":
        if element >= 0:
            filtered_list.append(element)
print(filtered_list)