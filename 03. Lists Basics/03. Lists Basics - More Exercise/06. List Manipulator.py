input_numbers = input().split()
numbers_list = []
for element in input_numbers:
    numbers_list.append(int(element))
command = input().split()

while command[0] != "end":
    if command[0] == "exchange":
        if 0 <= int(command[1]) < len(numbers_list):
            numbers_list = numbers_list[int(command[1]) + 1:] + numbers_list[:int(command[1]) + 1]
        else:
            print(f"Invalid index")
    else:
        even_numbers = []
        odd_numbers = []
        index_list_even = []
        index_list_odd = []

        for number in numbers_list:
            if number % 2 == 0:
                even_numbers.append(int(number))
            else:
                odd_numbers.append(int(number))

        if command[0] == "max":
            if command[1] == "even" and even_numbers:
                for index, value in enumerate(numbers_list):
                    if int(value) == max(even_numbers):
                        index_list_even.append(index)
                if len(index_list_even) == 1:
                    print(index_list_even[0])
                else:
                    print(index_list_even[-1])
            elif command[1] == "odd" and odd_numbers:
                for index, value in enumerate(numbers_list):
                    if int(value) == max(odd_numbers):
                        index_list_odd.append(index)
                if len(index_list_odd) == 1:
                    print(index_list_odd[0])
                else:
                    print(index_list_odd[-1])
            else:
                print("No matches")

        elif command[0] == "min":
            if command[1] == "even" and even_numbers:
                for index, value in enumerate(numbers_list):
                    if int(value) == min(even_numbers):
                        index_list_even.append(index)
                if len(index_list_even) == 1:
                    print(index_list_even[0])
                else:
                    print(index_list_even[-1])
            elif command[1] == "odd" and odd_numbers:
                for index, value in enumerate(numbers_list):
                    if int(value) == min(odd_numbers):
                        index_list_odd.append(index)
                if len(index_list_odd) == 1:
                    print(index_list_odd[0])
                else:
                    print(index_list_odd[-1])
            else:
                print("No matches")

        elif command[0] == "first":
            if 0 < int(command[1]) <= len(numbers_list):
                if command[2] == "even":
                    print(even_numbers[:int(command[1])])
                elif command[2] == "odd":
                    print(odd_numbers[:int(command[1])])
            else:
                print("Invalid count")

        elif command[0] == "last":
            if 0 < int(command[1]) <= len(numbers_list):
                if command[2] == "even":
                    if len(even_numbers) < int(command[1]):
                        print(even_numbers)
                    else:
                        print(even_numbers[-int(command[1]):])
                elif command[2] == "odd":
                    if len(odd_numbers) < int(command[1]):
                        print(odd_numbers)
                    else:
                        print(odd_numbers[-int(command[1]):])
            else:
                print("Invalid count")

    command = input().split()

print(numbers_list)
