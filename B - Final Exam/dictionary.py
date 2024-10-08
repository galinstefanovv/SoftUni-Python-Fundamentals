words_with_definition = input().split(" | ")
test_words = input().split(" | ")
command = input()
definition_dict = {}
for element in words_with_definition:
    new_list = element.split(": ")
    if new_list[0] not in definition_dict.keys():
        definition_dict[new_list[0]] = [new_list[1]]
    else:
        definition_dict[new_list[0]].append(new_list[1])

if command == "Test":
    for word, definition in sorted(definition_dict.items()):
        if word in test_words:
            print(f"{word}:")
            for text in definition:
                print(f" -{text}")
elif command == "Hand Over":
    for word, definition in definition_dict.items():
        print(word, end = " ")
