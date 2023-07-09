schedule = input().split(", ")
command = input()
while command != "course start":
    modification = command.split(":")[0]
    title = command.split(":")[1]
    if modification == "Add":
        if title not in schedule:
            schedule.append(title)
    elif modification == "Insert":
        insert_index = int(command.split(":")[2])
        if title not in schedule:
            schedule.insert(insert_index, title)
    elif modification == "Remove":
        if title in schedule:
            remove_index = schedule.index(title)
            if remove_index + 1 == len(schedule):
                schedule.pop()
            else:
                schedule.pop(remove_index)
                if schedule[remove_index] == f"{title}-Exercise":
                    schedule.pop(remove_index)
    elif modification == "Swap":
        first_title = title
        second_title = command.split(":")[2]
        if first_title in schedule and second_title in schedule:
            first_title_index = schedule.index(first_title)
            second_title_index = schedule.index(second_title)
            schedule[first_title_index], schedule[second_title_index] = \
                schedule[second_title_index], schedule[first_title_index]
    elif modification == "Exercise":
        if title in schedule:
            if f"{title}-Exercise" not in schedule:
                exercise_index = schedule.index(title) + 1
                schedule.insert(exercise_index, f"{title}-Exercise")
        else:
            schedule.append(title)
            schedule.append(f"{title}-Exercise")
    for lesson in schedule:
        exercise_letters = len("Exercise")
        if lesson[-exercise_letters:] == "Exercise":
            exercise_title = lesson[:-exercise_letters - 1]
            if schedule.index(exercise_title) + 1 == schedule.index(lesson):
                continue
            else:
                current_exercise_index = schedule.index(lesson)
                new_exercise_index = schedule.index(exercise_title) + 1
                if current_exercise_index > new_exercise_index:
                    schedule.pop(current_exercise_index)
                    schedule.insert(new_exercise_index, lesson)
                else:
                    schedule.insert(new_exercise_index, lesson)
                    schedule.pop(current_exercise_index)
                break
    command = input()
lesson_counter = 0
for element in schedule:
    lesson_counter += 1
    print(f"{lesson_counter}.{element}")
