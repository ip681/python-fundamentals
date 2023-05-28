number = int(input())
word = input()
full_list = []
filtered_list = []
for _ in range(number):
    input_string = input()
    full_list.append(input_string)
    if word in input_string:
        filtered_list.append(input_string)
print(full_list)
print(filtered_list)

