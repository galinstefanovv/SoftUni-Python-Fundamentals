n = int(input())
word = input()
empty_list = list()
filtered_list = list()
for i in range(n):
    strings = input()
    empty_list.append(strings)
    if word in strings:
        filtered_list.append(strings)
print(empty_list)
print(filtered_list)