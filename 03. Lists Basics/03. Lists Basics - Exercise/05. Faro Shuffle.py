input_string = input()
shuffles_count = int(input())
original_list = input_string.split(" ")
middle = int(len(original_list) / 2)
shuffled_string = original_list
for shuffle in range(shuffles_count):
    first_list = shuffled_string[0:middle]
    second_list = shuffled_string[middle:]
    shuffled_string = []
    for i in range(len(first_list)):
        shuffled_string.append(first_list[i])
        shuffled_string.append(second_list[i])
print(shuffled_string)

