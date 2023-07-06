command = input()
to_do_list = [0] * 10
while command != "End":
    tasks = command.split("-")
    current_task = tasks[1]
    priority = int(tasks[0])
    to_do_list.pop(priority - 1)
    to_do_list.insert(priority - 1, current_task)
    command = input()
final_list = [task for task in to_do_list if task != 0]
print(final_list)
