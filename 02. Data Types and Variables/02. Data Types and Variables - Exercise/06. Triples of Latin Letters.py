number_of_letters = int(input())

for first_char in range(number_of_letters):
    for second_char in range(number_of_letters):
        for third_char in range(number_of_letters):
            print(f"{chr(97 + first_char)}{chr(97 + second_char)}{chr(97 + third_char)}")
