my_list = [int(n) for n in input().split()]
average = sum([j for j in my_list]) / len(my_list)
second_list = sorted([k for k in my_list if k > average])
if len(second_list) < 1:
    print(f'No')
else:
    print(f"{' '.join(str(i) for i in second_list[:-6:-1])}")
