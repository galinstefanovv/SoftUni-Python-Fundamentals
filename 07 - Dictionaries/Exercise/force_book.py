force_side_dictionary = {}
command = input()

while command != "Lumpawaroo":
    if "|" in command:
        splitted_command = command.split(" | ")
        force_side, force_user = splitted_command
        user_is_part = False
        for value in force_side_dictionary.values():
            if force_user in value:
                user_is_part = True
                break
        if not user_is_part:
            if force_side not in force_side_dictionary.keys():
                force_side_dictionary[force_side] = [force_user]
            else:
                force_side_dictionary[force_side].append(force_user)
    elif "->" in command:
        splitted_command = command.split(" -> ")
        force_user, force_side = splitted_command
        for key, value in force_side_dictionary.items():
            if force_user in value:
                force_side_dictionary[key].pop(value.index(force_user))
                break
        if force_side not in force_side_dictionary.keys():
            force_side_dictionary[force_side] = [force_user]
        else:
            force_side_dictionary[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for force_side, force_users in force_side_dictionary.items():
    if len(force_users):
        print(f"Side: {force_side}, Members: {len(force_users)}")
        for user in force_users:
            print(f"! {user}")