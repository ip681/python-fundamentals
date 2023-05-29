people_sequence = input()
execution_number = int(input())
people_list = people_sequence.split(" ")
people_list = [int(x) for x in people_list]
executions_list = []
kill_counter = 0
current_index = 0

while len(people_list) > 0:
    kill_counter += 1

    if current_index >= len(people_list):
        current_index = 0

    if kill_counter % execution_number == 0:
        executions_list.append(people_list[current_index])
        people_list.pop(current_index)
        # executions_list.append(people_list.pop(index))
    else:
        current_index += 1

print(str(executions_list).replace(" ", ""))

