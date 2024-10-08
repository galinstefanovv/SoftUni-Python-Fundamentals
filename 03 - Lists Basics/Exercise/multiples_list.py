factor = int(input())
count = int(input())
my_list = []
for i in range(1, count + 1):
    elements = factor * i
    my_list.append(elements)
print(sorted(my_list))
