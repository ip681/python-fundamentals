def process_fr_list(friends_list, commands):
    blacklisted_names = 0
    lost_names = 0

    for command in commands:
        if command.startswith("Blacklist"):
            _, name = command.split(" ")
            if name in friends_list:
                friends_list = [n if n != name else "Blacklisted" for n in friends_list]
                blacklisted_names += 1
                print(f"{name} was blacklisted.")
            else:
                print(f"{name} was not found.")

        elif command.startswith("Error"):
            _, index = command.split(" ")
            index = int(index)
            if 0 <= index < len(friends_list) and friends_list[index] != "Blacklisted" and friends_list[index] != "Lost":
                name = friends_list[index]
                friends_list[index] = "Lost"
                lost_names += 1
                print(f"{name} was lost due to an error.")

        elif command.startswith("Change"):
            _, index, new_name = command.split(" ")
            index = int(index)
            if 0 <= index < len(friends_list):
                current_name = friends_list[index]
                friends_list[index] = new_name
                print(f"{current_name} changed his username to {new_name}.")

    return blacklisted_names, lost_names, friends_list


friends = input().split(", ")
commands = []
while True:
    command = input()
    if command == "Report":
        break
    commands.append(command)

blacklisted, lost, updated_friends = process_fr_list(friends, commands)
print(f"Blacklisted names: {blacklisted}")
print(f"Lost names: {lost}")
print(" ".join(updated_friends))