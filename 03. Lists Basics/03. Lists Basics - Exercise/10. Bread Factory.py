day_events = input()
energy = 100
coins = 100
day_events_list = day_events.split("|")
day_is_completed = True
for i in range(len(day_events_list)):
    current_event_string = day_events_list[i]
    current_event_list = current_event_string.split("-")
    current_event = current_event_list[0]
    current_value = int(current_event_list[1])
    if current_event == "rest":
        gained_energy = 0
        if energy >= 100:
            gained_energy = 0
        else:
            energy += current_value
            if energy > 100:
                gained_energy = current_value + (100 - energy)
                energy = 100
            else:
                gained_energy = current_value
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif current_event == "order":
        if (energy - 30) >= 0:
            energy -= 30
            coins += current_value
            print(f"You earned {current_value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if (coins - current_value) >= 0:
            coins -= current_value
            print(f"You bought {current_event}.")
        else:
            print(f"Closed! Cannot afford {current_event}.")
            day_is_completed = False
            break
if day_is_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

