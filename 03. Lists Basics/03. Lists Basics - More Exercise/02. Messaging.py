numbers_sequence = input()
input_string = input()
numbers_list = numbers_sequence.split(" ")
indices_list = []
final_message = ""
for index in range(len(numbers_list)):
    current_combination = numbers_list[index]
    current_sum = 0
    for sequence in range(len(current_combination)):
        current_sum += int(current_combination[sequence])
    indices_list.append(current_sum)
message_indices_count = len(input_string)
for symbol in range(len(numbers_list)):
    current_index = indices_list[symbol]
    while current_index > (message_indices_count - 1):
        current_index -= message_indices_count
    current_symbol = input_string[current_index]
    input_string = input_string[:current_index] + \
        input_string[current_index + 1::]
    final_message += current_symbol
print(final_message)
