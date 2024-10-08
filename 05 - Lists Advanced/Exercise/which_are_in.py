first = input().split(", ")
second = input().split(", ")
new_list = []
for first_element in range(len(first)):
    for second_element in range(len(second)):
        if first[first_element] in second[second_element] and not first[first_element] in new_list:
            new_list.append(first[first_element])
print(new_list)