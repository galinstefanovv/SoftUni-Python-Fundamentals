tail = input()
body = input()
head = input()
empty_list = [tail, body, head]
empty_list[0], empty_list[2] = empty_list[2], empty_list[0]
print(empty_list)
