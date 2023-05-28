number = int(input())
numbers_list = []
filtered_list = []
for _ in range(number):
    current_number = int(input())
    numbers_list.append(current_number)
command = input()
if command == "even":
    for n in numbers_list:
        if n % 2 == 0:
            filtered_list.append(n)
elif command == "odd":
    for n in numbers_list:
        if n % 2 != 0:
            filtered_list.append(n)
elif command == "negative":
    for n in numbers_list:
        if n < 0:
            filtered_list.append(n)
elif command == "positive":
    for n in numbers_list:
        if n >= 0:
            filtered_list.append(n)
print(filtered_list)

