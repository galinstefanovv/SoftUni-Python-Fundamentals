text = input()
empty = list()
for i in range(len(text)):
    if text[i].isupper():
        empty.append(i)

print(empty)