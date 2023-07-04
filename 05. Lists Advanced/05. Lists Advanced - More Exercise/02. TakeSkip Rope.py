def uncover_message(string, take, skip):
    final_message = ""
    for change in range(len(take)):
        take_num = take[change]
        skip_num = skip[change]
        final_message += string[:take_num]
        string = string[take_num:]
        string = string[skip_num:]
    return final_message


mixed_string = input()
digits_list = []
symbols_list = []
take_list = []
skip_list = []
for symbol in mixed_string:
    if symbol.isdigit():
        digits_list.append(int(symbol))
    else:
        symbols_list.append(symbol)
for index, digit in enumerate(digits_list):
    if index % 2 == 0:
        take_list.append(digit)
    else:
        skip_list.append(digit)
starting_string = "".join(symbols_list)
print(uncover_message(starting_string, take_list, skip_list))