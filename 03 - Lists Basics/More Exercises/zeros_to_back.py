my_list = input().split(", ")
new_list = []
count = 0
for element in my_list:
    new_list.append(int(element))
while 0 in new_list:
    new_list.remove(0)
    count += 1
for j in range(1, count + 1):
    new_list.append(0)
print(new_list)