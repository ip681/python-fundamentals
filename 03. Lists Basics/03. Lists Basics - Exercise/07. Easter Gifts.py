gifts_string = input()
gifts_list = gifts_string.split(" ")
command = input()
while command != "No Money":
    command_list = command.split(" ")
    command = command_list[0]
    gift = command_list[1]
    index = command_list[-1]
    if (gift != index) and (0 <= int(index) < len(gifts_list)):
        index_is_valid = True
    else:
        index_is_valid = False
    if command == "OutOfStock":
        for i in range(len(gifts_list)):
            if gifts_list[i] == gift:
                gifts_list[i] = "None"
    elif command == "Required":
        if index_is_valid:
            gifts_list[int(index)] = gift
    elif command == "JustInCase":
        gifts_list[-1] = gift
    command = input()
for g in range(len(gifts_list)):
    if gifts_list[g] != "None":
        print(gifts_list[g], end=" ")

