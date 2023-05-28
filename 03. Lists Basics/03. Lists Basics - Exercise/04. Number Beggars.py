integers_string = input()
beggars_count = int(input())
all_sums = integers_string.split(", ")
beggars_list = []
for beggar in range(beggars_count):
    current_sum = 0
    for i in range(len(all_sums)):
        if i == beggar:
            current_sum += int(all_sums[i])
            beggar += beggars_count
    beggars_list.append(current_sum)
print(beggars_list)


