numbers_sequence = input()
sequence_list = numbers_sequence.split(" ")
sequence_list = [int(i) for i in sequence_list]
middle_index = int(len(sequence_list) / 2)
left_car_time = float()
right_car_time = float()
for left_index in range(middle_index):
    current_left_time = sequence_list[left_index]
    if current_left_time == 0:
        left_car_time *= 0.80
    else:
        left_car_time += current_left_time
sequence_list.reverse()
for right_index in range(middle_index):
    current_right_time = sequence_list[right_index]
    if current_right_time == 0:
        right_car_time *= 0.80
    else:
        right_car_time += current_right_time
if left_car_time < right_car_time:
    winner = "left"
    winner_time = left_car_time
else:
    winner = "right"
    winner_time = right_car_time
print(f"The winner is {winner} with total time: {winner_time:.1f}")

