filter = input().split(' ')
# filtered_words = [word for word in filter if len(word) % 2 == 0]
# print(f"{'\n'.join(filtered_words)}")
for element in filter:
    if len(element) % 2 == 0:
        print(f'{element}')