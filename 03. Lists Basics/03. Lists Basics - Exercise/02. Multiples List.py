factor = int(input())
count = int(input())
output_list = [factor]
current_number = factor
for i in range(count - 1):
    current_number += factor
    output_list.append(current_number)
print(output_list)

