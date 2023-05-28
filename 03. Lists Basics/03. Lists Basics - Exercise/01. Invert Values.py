input_string = input()
first_list = input_string.split(" ")
second_list = []
for i in range(len(first_list)):
    new_value = int(first_list[i]) * -1
    second_list.append(new_value)
print(second_list)
