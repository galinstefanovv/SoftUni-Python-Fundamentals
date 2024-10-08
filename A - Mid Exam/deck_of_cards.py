# def add(card_name):
#     if card_name in cards:
#         print(f'Card is already in the deck')
#     else:
#         cards.append(card_name)
#         print(f'Card successfully added')
#     return cards
#
#
# def remove(card_name):
#     if card_name in cards:
#         cards.remove(card_name)
#         print(f'Card successfully removed')
#     else:
#         print(f'Card not found')
#     return cards
#
#
# def remove_at(index):
#     if index in range(len(cards)):
#         cards.pop(index)
#         print(f'Card successfully removed')
#     else:
#         print(f'Index out of range')
#     return cards
#
#
# def insert(index, card_name):
#     if index in range(len(cards)):
#         if card_name in cards:
#             print(f'Card is already added.')
#         else:
#             cards.insert(index, card_name)
#             print(f'Card successfully added')
#     else:
#         print(f'Index out of range')
#     return cards
#
#
# cards = input().split(", ")
# number = int(input())
#
# for i in range(1, number + 1):
#     command = input().split(', ')
#
#     if command[0] == "Add":
#         add(command[1])
#     elif command[0] == "Remove":
#         remove(command[1])
#     elif command[0] == "Remove At":
#         remove_at(int(command[1]))
#     elif command[0] == "Insert":
#         insert(int(command[1]), command[2])
#
# print(f"{', '.join(str(card) for card in cards)}")

cards = input().split(", ")
number = int(input())

for i in range(1, number + 1):
    command = input().split(", ")

    if command[0] == "Add":
        if not command[1] in cards:
            cards.append(command[1])
            print(f'Card successfully added')
        else:
            print(f'Card is already in the deck')
    elif command[0] == "Remove":
        if command[1] in cards:
            cards.remove(command[1])
            print(f'Card successfully removed')
        else:
            print(f'Card not found')
    elif command[0] == "Remove At":
        if int(command[1]) in range(len(cards)):
            cards.pop(int(command[1]))
            print(f'Card successfully removed')
        else:
            print(f'Index out of range')
    elif command[0] == "Insert":
        if int(command[1]) in range(len(cards)):
            if not command[2] in cards:
                cards.insert(int(command[1]), command[2])
                print(f'Card successfully added')
            else:
                print(f'Card is already added')
        else:
            print(f'Index out of range')
print(f"{', '.join(str(card) for card in cards)}")
